from fotoques.models import AlbumTemplate
from fotoques.models import UserAccount

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class AlbumTemplateAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        user = UserAccount(name="Cherny")
        albumTemplate = AlbumTemplate()
        albumTemplate.name = 'AlbumTemplate name'
        albumTemplate.userAcount = user.put()
        albumTemplate.maxPages = 9
        albumTemplate.PDFUrl = 'http://whatever'
        albumTemplate.size = [10, 15]
        albumTemplate.put()
        self.assertEqual(1, len(AlbumTemplate.all().fetch(1)))
    
    def testReadEntity(self):
        user = UserAccount(name="Cherny")
        albumTemplate = AlbumTemplate()
        albumTemplate.name = 'AlbumTemplate name'
        albumTemplate.userAcount = user.put()
        albumTemplate.maxPages = 9
        albumTemplate.PDFUrl = 'http://whatever'
        albumTemplate.size = [10, 15]
        albumTemplate.put()
        albumTemplateInserted = AlbumTemplate.all().fetch(1)[0]
        self.assertEqual(albumTemplate.name, albumTemplateInserted.name)
        
    def testUpdateEntity(self):
        user = UserAccount(name="Cherny")
        albumTemplate = AlbumTemplate()
        albumTemplate.name = 'AlbumTemplate name'
        albumTemplate.userAcount = user.put()
        albumTemplate.maxPages = 9
        albumTemplate.PDFUrl = 'http://whatever'
        albumTemplate.size = [10, 15]
        albumTemplate.put()
        albumTemplateInserted = AlbumTemplate.all().fetch(1)[0]
        albumTemplateInserted.name = 'Another albumTemplate name'
        albumTemplateInserted.put()
        albumTemplateUpdated = AlbumTemplate.all().fetch(1)[0]
        self.assertEqual(albumTemplateInserted.name , albumTemplateUpdated.name)
    
    def testDeleteEntity(self):
        user = UserAccount(name="Cherny")
        albumTemplate = AlbumTemplate()
        albumTemplate.name = 'AlbumTemplate name'
        albumTemplate.userAcount = user.put()
        albumTemplate.maxPages = 9
        albumTemplate.PDFUrl = 'http://whatever'
        albumTemplate.size = [10, 15]
        albumTemplate.put()
        albumTemplateInserted = AlbumTemplate.all().fetch(1)[0]
        albumTemplateInserted.name = 'Another albumTemplate name'
        albumTemplate.put()
        albumTemplateInserted = AlbumTemplate.all().fetch(1)[0]
        albumTemplateInserted.delete()
        self.assertEqual(len(AlbumTemplate.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()