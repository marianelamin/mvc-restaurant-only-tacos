from google.appengine.ext import ndb


class TacoFilling(ndb.Model):
    tacoIn = ndb.StringProperty(required=True)