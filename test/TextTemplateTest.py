from fotoques.models import Album
from fotoques.models import UserAccount

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class AlbumAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        user = UserAccount(name="Cherny")
        album = Album()
        album.name = 'Album name'
        album.userAcount = user.put()
        album.maxPages = 9
        album.PDFUrl = 'http://whatever'
        album.size = [10, 15]
        album.put()
        self.assertEqual(1, len(Album.all().fetch(1)))
    
    def testReadEntity(self):
        user = UserAccount(name="Cherny")
        album = Album()
        album.name = 'Album name'
        album.userAcount = user.put()
        album.maxPages = 9
        album.PDFUrl = 'http://whatever'
        album.size = [10, 15]
        album.put()
        albumInserted = Album.all().fetch(1)[0]
        self.assertEqual(album.name, albumInserted.name)
        
    def testUpdateEntity(self):
        user = UserAccount(name="Cherny")
        album = Album()
        album.name = 'Album name'
        album.userAcount = user.put()
        album.maxPages = 9
        album.PDFUrl = 'http://whatever'
        album.size = [10, 15]
        album.put()
        albumInserted = Album.all().fetch(1)[0]
        albumInserted.name = 'Another album name'
        albumInserted.put()
        albumUpdated = Album.all().fetch(1)[0]
        self.assertEqual(albumInserted.name , albumUpdated.name)
    
    def testDeleteEntity(self):
        user = UserAccount(name="ssss4545454545Cherny")
        album = Album()
        album.name = 'Album name'
        album.userAcount = user.put()
        album.maxPages = 9
        album.PDFUrl = 'http://whatever'
        album.size = [10, 15]
        album.put()
        albumInserted = Album.all().fetch(1)[0]
        albumInserted.name = 'Another album name'
        album.put()
        albumInserted = Album.all().fetch(1)[0]
        albumInserted.delete()
        self.assertEqual(len(Album.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()