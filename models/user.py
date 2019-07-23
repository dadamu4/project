from google.appengine.ext import ndb
from google.appengine.api import users

import datetime

class Comment(ndb.Model):
    date = datetime.datetime.now().strftime("%x")
    title = ndb.StringProperty(required = True)
    comment = ndb.StringProperty(required = True)

class User(ndb.Model):
    email = ndb.StringProperty(required = True)
    firstName = ndb.StringProperty(required = False)
    lastName = ndb.StringProperty(required = False)
    moneySpent = ndb.StringProperty(required = False)
    weeklyAllowance = ndb.StringProperty(required = False)
    savings = ndb.StringProperty(required = False)
    utilities = ndb.StringProperty(required = False)
    fun = ndb.StringProperty(required = False)
    comments = ndb.KeyProperty(Comment, repeated=True)