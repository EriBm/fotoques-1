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
        actives = (
                   'UserAccount',
                   'Album',
                   'AlbumTemplate',
                   )
        page = {}
        content = None
        path = self.request.path
        if path == '/admin/UserAccount':
            page = {'current' : 'userAccount', 'title' : 'User Account'}
            content = UserAccountForm()
        if path == '/admin':
            page = {'current' : 'home', 'title' : 'Home'}
            content = 'Home'
        template_values = {'page' : page, 'content' : content, 'server' : os.environ['SERVER_NAME']}
        path = os.path.join(os.path.dirname(__file__), 'templates/adminModel.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication([('/admin.*', Admin)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()