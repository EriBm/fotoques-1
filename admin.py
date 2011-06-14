# -*- coding: utf-8 -*-

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
        logging.info("------")
        logging.info(ImageTemplateForm.Meta.widgets)
        
        # List of links and their possible form object
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
        # Reduces the size of the objects (just for the viewing stuff)
        links = [{'name' : object['name'], 'url' : object['url']} for object in objects if object['active']]
        
        # Determine which element is called and do something
        path = self.request.path
        for object in objects:
            if not object['active']:
                continue
            if path == object['url']:
                current = object
                break
        server = os.environ['SERVER_NAME'] + str(':' + os.environ['SERVER_PORT']) if os.environ['SERVER_PORT'] != '80' else ''
        template_values = {'page' : current, 'server' : server, 'links' : links}
        path = os.path.join(os.path.dirname(__file__), 'templates/adminModel.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication([('/admin.*', Admin)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()