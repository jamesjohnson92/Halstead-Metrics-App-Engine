from google.appengine.ext import ndb

class Model(ndb.Model):

    username = ndb.StringProperty(required = True)

    password = ndb.StringProperty(required = True)

    firstname = ndb.StringProperty(required = True)

    lastname = ndb.StringProperty(required = True)


def generateRegisterationKey(username):
    return ndb.Key('Model',username)
