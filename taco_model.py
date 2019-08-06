#this line is very important because it lets us use the ndb.Model in the class
from google.appengine.ext import ndb


class TacoFilling(ndb.Model):
    # this is one property of type String
    tacoIn = ndb.StringProperty(required=True)