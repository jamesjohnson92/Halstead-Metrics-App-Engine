from gaesessions import get_current_session
from google.appengine.ext import blobstore
from Halstead import Halstead
import webapp2
import jinja2
import os

METRIC = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class ViewUploadHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        reader = blobstore.BlobReader(session['key'])
        content = reader.readlines()
        self.calculateHasteadMetrics(content)

    def calculateHasteadMetrics(self,content):
        metrics = Halstead(content)
        session = get_current_session()
        halsteadResult ={'Operators':metrics.getAllOperators(),
         'Operands':metrics.getAllOperands(),
         'NoUniOperators':metrics.getNoUniqueOperators(),
         'NoUniOperands':metrics.getNoUniqueOperands(),
         'NoAllOperators':metrics.getNoAllOperators(),
         'NoAllOperands':metrics.getNoAllOperands(),
         'Vocabulary':metrics.getVocabularySize(),
         'Length':metrics.getProgramLength(),
         'Volume':metrics.getVolume(),
         'Difficulty':metrics.getDifficulty(),
         'Effort':metrics.getEffort(),
         'user':session.get('user')
        }
        template = METRIC.get_template('./view/hmetricsoutput.html')
        self.response.write(template.render(halsteadResult))




