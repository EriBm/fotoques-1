from fotoques.models import Base

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class BaseAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        base = Base()
        base.name = 'Base name'
        base.put()
        self.assertEqual(1, len(Base.all().fetch(1)))
    
    def testReadEntity(self):
        base = Base()
        base.name = 'Base name'
        base.put()
        baseInserted = Base.all().fetch(1)[0]
        self.assertEqual(base.name, baseInserted.name)
        
    def testUpdateEntity(self):
        base = Base()
        base.name = 'Base name'
        base.put()
        baseInserted = Base.all().fetch(1)[0]
        baseInserted.name = 'Another base name'
        baseInserted.put()
        baseUpdated = Base.all().fetch(1)[0]
        self.assertEqual(baseInserted.name , baseUpdated.name)
    
    def testDeleteEntity(self):
        base = Base()
        base.name = 'Base name'
        base.put()
        baseInserted = Base.all().fetch(1)[0]
        baseInserted.delete()
        self.assertEqual(len(Base.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()