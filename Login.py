from google.appengine.ext import ndb
from gaesessions import get_current_session
from Model import Model
from urlparse import urlparse
import webapp2
import urllib2
import jinja2
import os


JINJAENVIRONMENT = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)


class Login(webapp2.RequestHandler):

    def post(self):
        self.login()

    def login(self):

        username = self.request.get('username')

        password = self.request.get('password')

        query = "SELECT * FROM Model WHERE username = :1 and password = :2"

        entity = ndb.gql(query,username,password)

        if entity :
            err = {'error':'Your Username and Password is wrong'}
            template = JINJAENVIRONMENT.get_template('./view/loginerror.html')
            self.response.write(template.render(err))

        UserIdentity = {'username':username}

        parsed_url = urlparse(self.request.uri)

        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)

        session = get_current_session()

        session['user'] = username

        for user in entity:
            self.redirect(domain+"aboutgae")

