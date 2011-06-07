from models import *

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        userAccount = UserAccount()
        base = Base()
        album = Album()
        albumTemplate = AlbumTemplate()
        image = Image()
        imageTemplate = ImageTemplate()
        page = Page()
        pageTemplate = PageTemplate()
        text = Text()
        text = TextTemplate()
        self.response.out.write('funciona :)')

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()