import webapp2
import os
import jinja2
from models.user import User, Comment
from google.appengine.api import users
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LogInPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
          signout_link_html = users.create_logout_url('/')
          email_address = user.nickname()
          appUser = User.query().filter(User.email == email_address).get()
          if appUser:
              return webapp2.redirect('/home')
          else:
            # Registration form for a first-time visitor:
            return webapp2.redirect('/register')

        else:
          # If the user isn't logged in...
          login_url = users.create_login_url('/')
          start_template = jinja_env.get_template("html/login.html")
          self.response.write(start_template.render({"url": login_url}))


class RegisterPage(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("html/register.html")
        self.response.write(start_template.render())

    def post(self):
        user = users.get_current_user()
        appUser = User(
            firstName = self.request.get('first_name'),
            lastName = self.request.get('last_name'),
            email = user.nickname())
        appUser.put()
        start_template = jinja_env.get_template("html/thanks.html")
        self.response.write(start_template.render({"name": appUser.firstName}))

class HomePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        signout_link_html = users.create_logout_url('/')
        start_template = jinja_env.get_template("html/main.html")
        self.response.write(start_template.render({"signOut": signout_link_html}))

app = webapp2.WSGIApplication([
    ('/', LogInPage),
    ('/register', RegisterPage),
    ('/home', HomePage),
])
