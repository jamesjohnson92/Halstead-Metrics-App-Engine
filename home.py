from google.appengine.api import users
from gaesessions import get_current_session
import jinja2
import webapp2
import os

HOME = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class Home(webapp2.RequestHandler):

    def get(self):
        self.redirect('/uploadform')
