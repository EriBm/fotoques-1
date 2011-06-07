from google.appengine.ext import db
from google.appengine.ext.db import polymodel
import appengine_admin

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

class Base(polymodel.PolyModel):
    name = db.StringProperty()
    createdAt = db.DateTimeProperty(auto_now_add=True)
    updatedAt = db.DateTimeProperty(auto_now=True)

class Album(Base):
    userAccount = db.ReferenceProperty(UserAccount)
    maxPages = db.IntegerProperty()
    PDFUrl = db.LinkProperty()
    size = db.ListProperty(int) # [width, height]

class AlbumTemplate(Album):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='AlbumTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='AlbumTemplateUpdated')

class Image(Base):
    userAccount = db.UserProperty()
    picasaID = db.StringProperty()
    picasaThumbnailUrl = db.LinkProperty()
    size = db.ListProperty(int) # [width, height]
    css = db.StringProperty()

    def __init__(self):
        self.css = "{margin: 0px; position: absolute}"
    
class ImageTemplate(Image):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='ImageTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='ImageTemplateUpdated')

class Page(Base):
    pageNumber = db.IntegerProperty()
    userAccount = db.UserProperty()
    css = db.StringProperty()

class PageTemplate(Page):
    createdBy = db.ReferenceProperty(UserAccount, collection_name='PageTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='PageTemplateUpdated')

class Text(Base):
    userAccount = db.UserProperty()
    text = db.StringProperty()
    css = db.StringProperty()

class TextTemplate():
    createdBy = db.ReferenceProperty(UserAccount, collection_name='TextTemplateCreated')
    updatedBy = db.ReferenceProperty(UserAccount, collection_name='TextTemplateUpdated')

class AdminUser(appengine_admin.ModelAdmin):
    model = UserAccount
    listFields = ('name', 'email', 'googleToken')
#    editFields = ('title', 'content')
#    readonlyFields = ('whencreated', 'whenupdated')

appengine_admin.register(AdminUser)