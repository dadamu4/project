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
          signout_link_html = '<a href="%s">sign out</a>' % (
                    users.create_logout_url('/'))
          email_address = user.nickname()
          appUser = User.query().filter(User.email == email_address).get()
          if appUser:
              return webapp2.redirect('/home')
              self.response.write(start_template.render({"signOut": signout_link_html}))
          else:
            # Registration form for a first-time visitor:
            self.response.write('''
                Welcome to our site, %s!  Please sign up! <br>
                <form method="post" action="/">
                <input type="text" name="first_name">
                <input type="text" name="last_name">
                <input type="submit">
                </form><br> %s <br>
                ''' % (email_address, signout_link_html))

        else:
          # If the user isn't logged in...
          login_url = users.create_login_url('/')
          login_html_element = '<a href="%s">Sign in</a>' % login_url
          self.response.write('Please log in.<br>' + login_html_element)

    def post(self):
        # Code to handle a first-time registration from the form:
        user = users.get_current_user()
        appUser = User(
            firstName=self.request.get('first_name'),
            lastName=self.request.get('last_name'),
            email=user.nickname())
        appUser.put()
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
            appUser.firstName)

class HomePage(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("html/main.html")

app = webapp2.WSGIApplication([
    ('/', LogInPage),
    ('/home', HomePage)
], debug=True)
