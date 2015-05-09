from Model import Model
from Model import generateRegisterationKey
from google.appengine.ext import ndb
import jinja2
import sys
import webapp2
import os

RegisterHTML = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

class Register(webapp2.RequestHandler):

    def post(self):

       self.username = self.request.get('username')

       password = self.request.get('password')

       confirmpassword = self.request.get('confirmpassword')

       if password  in confirmpassword:
           self.password = password
       else:
           error = "##### Registeration Error : Please type Same Password "
           notify = {'error':error}
           template = RegisterHTML.get_template('./view/error.html')
           self.response.write(template.render(notify))

       self.firstname = self.request.get('firstname')

       self.lastname = self.request.get('lastname')

       self.runRegistrationForUser()




    def runRegistrationForUser(self):


        register = Model(key = generateRegisterationKey(self.username))

        register.firstname = self.firstname

        register.lastname = self.lastname

        register.username = self.username

        register.password = self.password

        register.put()

        template = RegisterHTML.get_template('./view/login.html')
        self.response.write(template.render())



