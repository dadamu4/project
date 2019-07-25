from google.appengine.ext import ndb
from google.appengine.api import users

import datetime

class User(ndb.Model):
    email = ndb.StringProperty(required = True)
    firstName = ndb.StringProperty(required = False)
    lastName = ndb.StringProperty(required = False)

class FinancialComment(ndb.Model):
    date = datetime.datetime.now().strftime("%x")
    owner = ndb.KeyProperty(User)
    ownerName = ndb.StringProperty(required = True)
    comment = ndb.StringProperty(required = True)

class Financials(ndb.Model):
    owner = ndb.KeyProperty(User)
    stocks = ndb.StringProperty(required = False, repeated=True)
    # weeklyAllowance = ndb.StringProperty(required = False)
    # savings = ndb.StringProperty(required = False)
    # utilities = ndb.StringProperty(required = False)
    # fun = ndb.StringProperty(required = False)
