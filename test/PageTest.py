from fotoques.models import Page
from fotoques.models import UserAccount

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class PageAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        user = UserAccount(name="Cherny")
        page = Page()
        page.name = 'Page name'
        page.pageNumber = 12
        page.maxPages = 9
        page.PDFUrl = 'http://whatever'
        page.size = [10, 15]
        page.put()
        self.assertEqual(1, len(Page.all().fetch(1)))
    
    def testReadEntity(self):
        user = UserAccount(name="Cherny")
        page = Page()
        page.name = 'Page name'
        page.userAcount = user.put()
        page.maxPages = 9
        page.PDFUrl = 'http://whatever'
        page.size = [10, 15]
        page.put()
        pageInserted = Page.all().fetch(1)[0]
        self.assertEqual(page.name, pageInserted.name)
        
    def testUpdateEntity(self):
        user = UserAccount(name="Cherny")
        page = Page()
        page.name = 'Page name'
        page.userAcount = user.put()
        page.maxPages = 9
        page.PDFUrl = 'http://whatever'
        page.size = [10, 15]
        page.put()
        pageInserted = Page.all().fetch(1)[0]
        pageInserted.name = 'Another page name'
        pageInserted.put()
        pageUpdated = Page.all().fetch(1)[0]
        self.assertEqual(pageInserted.name , pageUpdated.name)
    
    def testDeleteEntity(self):
        user = UserAccount(name="Cherny")
        page = Page()
        page.name = 'Page name'
        page.userAcount = user.put()
        page.maxPages = 9
        page.PDFUrl = 'http://whatever'
        page.size = [10, 15]
        page.put()
        pageInserted = Page.all().fetch(1)[0]
        pageInserted.name = 'Another page name'
        page.put()
        pageInserted = Page.all().fetch(1)[0]
        pageInserted.delete()
        self.assertEqual(len(Page.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()