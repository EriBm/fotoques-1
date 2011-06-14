from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from validators import *

class UserAccount(db.Model):
    name = db.StringProperty(validator=Alpha, verbose_name="Name", required=True)
    email = db.EmailProperty(verbose_name="Email")
    googleToken = db.StringProperty(verbose_name="Google Token")
    facebookToken = db.StringProperty(verbose_name="Facebok Token")
    flickrToken = db.StringProperty(verbose_name="Flickr Token")
    password = db.StringProperty(verbose_name="Password")
    createdAt = db.DateTimeProperty(auto_now_add=True, verbose_name="Created At")
    updatedAt = db.DateTimeProperty(auto_now=True, verbose_name="Update At")
    address1 = db.StringProperty(verbose_name="Address 1")
    address2 = db.StringProperty(verbose_name="Address 2")
    phone1 = db.PhoneNumberProperty(verbose_name="Phone 1")
    phone2 = db.PhoneNumberProperty(verbose_name="Phone 2")
    documentID = db.IntegerProperty(verbose_name="Document ID")
    
    def __unicode__(self):
        return self.name

class Base(polymodel.PolyModel):
    name = db.StringProperty()
    createdAt = db.DateTimeProperty(auto_now_add=True)
    updatedAt = db.DateTimeProperty(auto_now=True)

class Album(Base):
    userAccount = db.ReferenceProperty(UserAccount, collection_name='Album')
    maxPages = db.IntegerProperty()
    PDFUrl = db.LinkProperty()
    size = db.ListProperty(int) # [width, height]
    
    def __unicode__(self):
        return self.name
    
class AlbumTemplate(Album):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='AlbumTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='AlbumTemplateUpdated')
    
    def __unicode__(self):
        return self.name

class Image(Base):
    userAccount = db.ReferenceProperty(UserAccount, collection_name="Image")
    picasaID = db.StringProperty()
    picasaThumbnailUrl = db.LinkProperty()
    size = db.ListProperty(int) # [width, height]
    css = db.StringProperty()
    page = db.StringListProperty() # Page references
    
    def __unicode__(self):
        return self.name

#    def __init__(self):
#        self.css = "{margin: 0px; position: absolute}"
    
class ImageTemplate(Image):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='ImageTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='ImageTemplateUpdated')

class Page(Base):
    pageNumber = db.IntegerProperty()
    userAccount = db.UserProperty()
    css = db.StringProperty()
    album = db.StringListProperty() # Album references

class PageTemplate(Page):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='PageTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='PageTemplateUpdated')

class Text(Base):
    userAccount = db.UserProperty()
    text = db.StringProperty()
    css = db.StringProperty()
    page = db.StringListProperty() # Page references

class TextTemplate(Text):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='TextTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='TextTemplateUpdated')