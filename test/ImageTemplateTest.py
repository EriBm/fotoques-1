from fotoques.models import ImageTemplate
from fotoques.models import UserAccount

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class ImageTemplateAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        user = UserAccount(name="Cherny")
        imageTemplate = ImageTemplate()
        imageTemplate.name = 'ImageTemplate name'
        imageTemplate.userAccount = user.put()
        imageTemplate.picasaID = 'http://whatever'
        imageTemplate.ThumbnaiUrl = 'http://whatever'
        imageTemplate.size = [10, 15]
        imageTemplate.css = '{rule : property;}'
        imageTemplate.put()
        self.assertEqual(1, len(ImageTemplate.all().fetch(1)))
    
    def testReadEntity(self):
        user = UserAccount(name="Cherny")
        imageTemplate = ImageTemplate()
        imageTemplate.name = 'ImageTemplate name'
        imageTemplate.userAccount = user.put()
        imageTemplate.picasaID = 'http://whatever'
        imageTemplate.ThumbnaiUrl = 'http://whatever'
        imageTemplate.size = [10, 15]
        imageTemplate.css = '{rule : property;}'
        imageTemplate.put()
        imageTemplateInserted = ImageTemplate.all().fetch(1)[0]
        self.assertEqual(imageTemplate.name, imageTemplateInserted.name)
        
    def testUpdateEntity(self):
        user = UserAccount(name="Cherny")
        imageTemplate = ImageTemplate()
        imageTemplate.name = 'ImageTemplate name'
        imageTemplate.userAccount = user.put()
        imageTemplate.picasaID = 'http://whatever'
        imageTemplate.ThumbnaiUrl = 'http://whatever'
        imageTemplate.size = [10, 15]
        imageTemplate.css = '{rule : property;}'
        imageTemplate.put()
        imageTemplateInserted = ImageTemplate.all().fetch(1)[0]
        imageTemplateInserted.name = 'Another imageTemplate name'
        imageTemplateInserted.put()
        imageTemplateUpdated = ImageTemplate.all().fetch(1)[0]
        self.assertEqual(imageTemplateInserted.name , imageTemplateUpdated.name)
    
    def testDeleteEntity(self):
        user = UserAccount(name="Cherny")
        imageTemplate = ImageTemplate()
        imageTemplate.name = 'ImageTemplate name'
        imageTemplate.userAccount = user.put()
        imageTemplate.picasaID = 'http://whatever'
        imageTemplate.ThumbnaiUrl = 'http://whatever'
        imageTemplate.size = [10, 15]
        imageTemplate.css = '{rule : property;}'
        imageTemplate.put()
        imageTemplateInserted = ImageTemplate.all().fetch(1)[0]
        imageTemplateInserted.name = 'Another imageTemplate name'
        imageTemplate.put()
        imageTemplateInserted = ImageTemplate.all().fetch(1)[0]
        imageTemplateInserted.delete()
        self.assertEqual(len(ImageTemplate.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()