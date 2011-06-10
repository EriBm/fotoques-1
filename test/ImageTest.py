from fotoques.models import Image
from fotoques.models import UserAccount

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class ImageAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        user = UserAccount(name="Cherny")
        image = Image()
        image.name = 'Image name'
        image.userAccount = user.put()
        image.picasaID = 'http://whatever'
        image.ThumbnaiUrl = 'http://whatever'
        image.size = [10, 15]
        image.css = '{rule : property;}'
        image.put()
        self.assertEqual(1, len(Image.all().fetch(1)))
    
    def testReadEntity(self):
        user = UserAccount(name="Cherny")
        image = Image()
        image.name = 'Image name'
        image.userAccount = user.put()
        image.picasaID = 'http://whatever'
        image.ThumbnaiUrl = 'http://whatever'
        image.size = [10, 15]
        image.css = '{rule : property;}'
        image.put()
        imageInserted = Image.all().fetch(1)[0]
        self.assertEqual(image.name, imageInserted.name)
        
    def testUpdateEntity(self):
        user = UserAccount(name="Cherny")
        image = Image()
        image.name = 'Image name'
        image.userAccount = user.put()
        image.picasaID = 'http://whatever'
        image.ThumbnaiUrl = 'http://whatever'
        image.size = [10, 15]
        image.css = '{rule : property;}'
        image.put()
        imageInserted = Image.all().fetch(1)[0]
        imageInserted.name = 'Another image name'
        imageInserted.put()
        imageUpdated = Image.all().fetch(1)[0]
        self.assertEqual(imageInserted.name , imageUpdated.name)
    
    def testDeleteEntity(self):
        user = UserAccount(name="Cherny")
        image = Image()
        image.name = 'Image name'
        image.userAccount = user.put()
        image.picasaID = 'http://whatever'
        image.ThumbnaiUrl = 'http://whatever'
        image.size = [10, 15]
        image.css = '{rule : property;}'
        image.put()
        imageInserted = Image.all().fetch(1)[0]
        imageInserted.name = 'Another image name'
        image.put()
        imageInserted = Image.all().fetch(1)[0]
        imageInserted.delete()
        self.assertEqual(len(Image.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()