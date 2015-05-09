from Login import Login
from UploadFormHandler import UploadFormHandler
from FileUploadHandler import FileUploadHandler
from Halstead import Halstead
from home import Home
from linerender import LineRender
from Register import Register
from ViewUploadHandler import ViewUploadHandler
from lineMetrics import lineMetric
from aboutgae import GoogleAppEngine
from aboutmcs import AboutMetrics
from lineresults import LineResults
from Logout import Logout
import webapp2
import jinja2
import os

MAINPAGE = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape=True)

class Main(webapp2.RequestHandler):
    """get"""
    def get(self):
        template = MAINPAGE.get_template('./view/login.html')
        self.response.write(template.render())


application = webapp2.WSGIApplication([
    ('/',Main),
    ('/login',Login),
    ('/register',Register),
    ('/reg',Register),
    ('/home',Home),
    ('/uploadform',UploadFormHandler),
    ('/upload',FileUploadHandler),
    ('/view',ViewUploadHandler),
    ('/lineMetric',lineMetric),
    ('/aboutmcs',AboutMetrics),
    ('/aboutgae',GoogleAppEngine),
    ('/line',LineRender),
    ('/result',LineResults),
    ('/logout',Logout),
    ],debug = True)

