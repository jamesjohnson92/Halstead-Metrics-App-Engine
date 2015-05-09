from google.appengine.api import users
from gaesessions import get_current_session
import jinja2
import webapp2
import os

LINERESULTS = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class LineResults(webapp2.RequestHandler):

    def get(self):
      template =   LINERESULTS.get_template('./view/locoutput.html')
      session = get_current_session()
      results = session.get('results')
      details = {'user':session.get('user'),'line':results['line'],'comment':results['comment']}
      self.response.write(template.render(details))
