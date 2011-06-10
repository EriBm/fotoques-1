from fotoques.models import UserAccount

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import unittest
from google.appengine.ext import testbed

class UserAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testCreatetentity(self):
        user = UserAccount(name="Cherny")
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
        user.put()
        self.assertEqual(1, len(UserAccount.all().fetch(1)))
    
    def testReadEntity(self):
        user = UserAccount(name="Cherny")
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
        user.put()
        userInserted = UserAccount.all().fetch(1)[0]
        self.assertEqual(user.name, userInserted.name)
        self.assertEqual(user.email, userInserted.email)
        self.assertEqual(user.googleToken, userInserted.googleToken)
        self.assertEqual(user.facebookToken, userInserted.facebookToken)
        self.assertEqual(user.flickrToken, userInserted.flickrToken)
        self.assertEqual(user.password, userInserted.password)
        self.assertEqual(user.address1, userInserted.address1)
        self.assertEqual(user.address2, userInserted.address2)
        self.assertEqual(user.phone1, userInserted.phone1)
        self.assertEqual(user.phone2, userInserted.phone2)
        self.assertEqual(user.documentID, userInserted.documentID)
        
    def testUpdateEntity(self):
        user = UserAccount(name="Cherny")
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
        user.put()
        userInserted = UserAccount.all().fetch(1)[0]
        userInserted.name = 'Erica'
        userInserted.put()
        userUpdated = UserAccount.all().fetch(1)[0]
        self.assertEqual(userInserted.name , userUpdated.name)
    
    def testDeleteEntity(self):
        user = UserAccount(name="Cherny")
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
        user.put()
        userInserted = UserAccount.all().fetch(1)[0]
        userInserted.delete()
        self.assertEqual(len(UserAccount.all().fetch(1)), 0)
        
class MainPage(webapp.RequestHandler):
    def get(self):
        pass

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()