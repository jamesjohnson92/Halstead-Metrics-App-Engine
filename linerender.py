from google.appengine.api import users
from gaesessions import get_current_session
import jinja2
import webapp2
import os

LINEMETRICS = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class LineRender(webapp2.RequestHandler):

    def get(self):
      template =   LINEMETRICS.get_template('./view/locinput.html')
      session = get_current_session()
      user = {'user':session.get('user')}
      self.response.write(template.render(user))
