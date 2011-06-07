from models import *

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class UserAccount(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    googleToken = db.StringProperty()
    facebookToken = db.StringProperty()
    flickrToken = db.StringProperty()
    password = db.StringProperty()
    createdAt = db.DateTimeProperty(auto_now_add=True)
    updatedAt = db.DateTimeProperty(auto_now=True)
    address1 = db.StringProperty()
    address2 = db.StringProperty()
    phone1 = db.PhoneNumberProperty()
    phone2 = db.PhoneNumberProperty()
    documentID = db.IntegerProperty()

class UserAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testInsertentity(self):
        user = UserAccount()
        user.name = 'Cherny D. C. Berbesi I.'
        user.email = 'cherny.berbesi@gmail.com'
        user.googleToken = '12345678901234567890'
        user.facebookToken = '12345678901234567890'
        user.flickrToken = '12345678901234567890'
        user.password = 'this_is_very_secret'
        user.address1 = 'somewhere in Venezuela'
        user.address2 = 'somewhere in San Cristobal'
        user.phone1 = '+582763423450'
        user.phone2 = '+584129381790'
        user.documentID = 15106061
        user.save()
        self.assertEqual(1, len(UserAccount.all().fetch(1)))
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()