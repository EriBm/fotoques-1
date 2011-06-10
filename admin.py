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
        page = {}
        content = None
        logging.info(self.request.path[7:])
        if self.request.path is 'admin' or self.request.path is 'admin/':
            page = {current : 'home', title : 'Home'}
        path = self.request.path[7:]
        logging.info('UserAccount')
        logging.info(path)
        if path == 'UserAccount':
            logging.info('UserAccount')
            logging.info(path)
            page = {'current' : 'userAccount', 'title' : 'Home'}
            content = UserAccountForm()
        if not page: # TODO Redirect to NOT_FOUND
            pass
        template_values = {'page' : page, 'content' : content}
        path = os.path.join(os.path.dirname(__file__), 'templates/adminModel.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication([('/admin.*', Admin)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()