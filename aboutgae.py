from google.appengine.api import users
from gaesessions import get_current_session
import jinja2
import webapp2
import os

AGAE = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class GoogleAppEngine(webapp2.RequestHandler):
    """get"""
    def get(self):
      template =   AGAE.get_template('./view/aboutGAE.html')
      session = get_current_session()
      user = {'user':session.get('user')}
      self.response.write(template.render(user))
