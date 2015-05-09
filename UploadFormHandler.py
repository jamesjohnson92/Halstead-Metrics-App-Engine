from google.appengine.ext import blobstore
from gaesessions import get_current_session
from Halstead import Halstead
import webapp2
import jinja2
import os

UPLOAD = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)


class UploadFormHandler(webapp2.RequestHandler):
    def get(self):
        url = blobstore.create_upload_url('/upload')
        session = get_current_session()
        user = session.get('user')
        carrier = {'url':url,'user':user}
        template = UPLOAD.get_template('./view/hmetricsinput.html')
        self.response.write(template.render(carrier))

