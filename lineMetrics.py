from gaesessions import get_current_session
import re
import webapp2
import jinja2
import os

exp = re.compile('^\s*?[/*|//|#][*]*.*?');
inc = re.compile('^/s*?[^#include][*]*.*?')

LINEMETRIC = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True);



class lineMetric(webapp2.RequestHandler):

    def post(self):
        self.linecount = 0
        self.commentcount = 0
        content = self.request.POST.get('file').file.readlines()
        self.parse(content)
        self.printPage()

    def parse(self,content):
        for line in content:
            self.linecount += 1
            if exp.match(line) and inc.match(line):
                self.commentcount += 1

    def getLineCount(self):
        return self.linecount

    def getCommentCount(self):
        return self.commentcount

    def printPage(self):
        results = {'line':self.getLineCount(),'comment':self.getCommentCount()}
        session = get_current_session()
        session['results'] = results

        self.redirect('/result')
        """
        template = LINEMETRIC.get_template('./view/locoutput.html')
        self.response.write(template.render(results))
        """
