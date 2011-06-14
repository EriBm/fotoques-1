import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'fotoques.settings'
from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from models import *
import logging

class UserAccountForm(djangoforms.ModelForm):
    class Meta:
        model = UserAccount
        exclude = ['googleToken', 'facebookToken', 'flickrToken', 'createdAt', 'updatedAt']

class AlbumForm(djangoforms.ModelForm):
    class Meta:
        model = Album
        exclude = ['_class', 'createdAt', 'updatedAt']

class ImageForm(djangoforms.ModelForm):
    class Meta:
        model = Image
        exclude = ['_class', 'createdAt', 'updatedAt']
        
class PageForm(djangoforms.ModelForm):
    class Meta:
        model = Page
        exclude = ['_class', 'createdAt', 'updatedAt']

class TextForm(djangoforms.ModelForm):
    class Meta:
        model = Text
        exclude = ['_class', 'createdAt', 'updatedAt', 'createdBy', 'updatedBy']

class AlbumTemplateForm(djangoforms.ModelForm):
    class Meta:
        model = AlbumTemplate
        exclude = ['_class', 'createdAt', 'updatedAt', 'createdBy', 'updatedBy', 'userAccount']

class ImageTemplateForm(djangoforms.ModelForm):
    class Meta:
        model = ImageTemplate
        exclude = ['_class', 'createdAt', 'updatedAt', 'createdBy', 'updatedBy', 'userAccount']
        widgets = {
            'size': djangoforms.forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class PageTemplateForm(djangoforms.ModelForm):
    class Meta:
        model = PageTemplate
        exclude = ['_class', 'createdAt', 'updatedAt', 'createdBy', 'updatedBy', 'userAccount']

class TextTemplateForm(djangoforms.ModelForm):
    class Meta:
        model = TextTemplate
        exclude = ['_class', 'createdAt', 'updatedAt', 'createdBy', 'updatedBy', 'userAccount']