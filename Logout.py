import webapp2
import jinja2
import os

LOGOUT = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class Logout(webapp2.RequestHandler):

    def get(self):
        self.redirect('/')

