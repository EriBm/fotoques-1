from models import *
from forms import *
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'fotoques.settings'
from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.db import djangoforms
import logging

class Admin(webapp.RequestHandler):
    def get(self):
        objects = [
                   {'name' : 'Home', 'url' : '/admin', 'active' : True},
                   {'name' : 'User Account', 'url' : '/admin/useraccount', 'form' : UserAccountForm(), 'active' : True},
                   {'name' : 'Album', 'url' : '/admin/album', 'form' : AlbumForm(), 'active' : True},
                   {'name' : 'Image', 'url' : '/admin/image', 'form' : ImageForm(), 'active' : True},
                   {'name' : 'Page', 'url' : '/admin/page', 'form' : PageForm(), 'active' : True},
                   {'name' : 'Text', 'url' : '/admin/text', 'form' : TextForm(), 'active' : True},
                   {'name' : 'AlbumTemplate', 'url' : '/admin/albumtemplate', 'form' : AlbumTemplateForm(), 'active' : True},
                   {'name' : 'ImageTemplate', 'url' : '/admin/imagetemplate', 'form' : ImageTemplateForm(), 'active' : True},
                   {'name' : 'PageTemplate', 'url' : '/admin/pagetemplate', 'form' : PageTemplateForm(), 'active' : True},
                   {'name' : 'TextTemplate', 'url' : '/admin/texttemplate', 'form' : TextTemplateForm(), 'active' : True}
                   ]
        path = self.request.path
        template_values = None
        for object in objects:
            if path == object['url']:
                template_values = object
                break
        path = os.path.join(os.path.dirname(__file__), 'templates/adminModel.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication([('/admin.*', Admin)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()