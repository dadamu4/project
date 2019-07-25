import webapp2
import os
import jinja2
import json
from models.user import User, FinancialComment, VoteComment, EnvComment
from google.appengine.api import users, urlfetch
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

class StockPage(webapp2.RequestHandler):
    def get(self):
        # apiurl = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=214DOVCITS6H4K3T"
        # apiresponse= urlfetch.fetch(apiurl).content
        # apijson = json.loads(apiresponse)
        user = users.get_current_user()
        email_address = user.nickname()
        appUser = User.query().filter(User.email == email_address).get()

        allDeStocks = FinancialComment.query().fetch()
        stock_template = jinja_env.get_template("html/financial.html")
        self.response.write(stock_template.render({"allStockComments": allDeStocks}))

    def post(self):
        comment = self.request.get('comment')
        user = users.get_current_user()
        email_address = user.nickname()
        appUser = User.query().filter(User.email == email_address).get()

        FinancialComment(owner = appUser.key, ownerName = appUser.firstName, comment = comment).put()

        allDeStocks = FinancialComment.query().fetch()

        stock_template = jinja_env.get_template("html/financialMadeComment.html")
        self.response.write(stock_template.render({"allStockComments": allDeStocks, "appUser": appUser.firstName, "comment": comment}))

class VotePage(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        email_address = user.nickname()
        appUser = User.query().filter(User.email == email_address).get()


        allVoteComments = VoteComment.query().fetch()
        vote_template = jinja_env.get_template("html/vote.html")
        self.response.write(vote_template.render({"allVoteComments": allVoteComments}))



    def post(self):
        user = users.get_current_user()
        email_address = user.nickname()
        appUser = User.query().filter(User.email == email_address).get()
        comment = self.request.get('comment')

        VoteComment(owner = appUser.key, ownerName = appUser.firstName, comment = comment).put()

        allVoteComments = VoteComment.query().fetch()

        vote_template = jinja_env.get_template("html/voteMadeComment.html")
        self.response.write(vote_template.render({"allVoteComments": allVoteComments, "appUser": appUser.firstName, "comment" : comment}))

class EnvironmentPage(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        email_address = user.nickname()
        appUser = User.query().filter(User.email == email_address).get()


        allEnvComments = EnvComment.query().fetch()
        env_template = jinja_env.get_template("html/environment.html")
        self.response.write(env_template.render({"allEnvComments": allEnvComments}))



    def post(self):
        user = users.get_current_user()
        email_address = user.nickname()
        appUser = User.query().filter(User.email == email_address).get()
        comment = self.request.get('comment')

        EnvComment(owner = appUser.key, ownerName = appUser.firstName, comment = comment).put()

        allEnvComments = EnvComment.query().fetch()

        env_template = jinja_env.get_template("html/envMadeComment.html")
        self.response.write(env_template.render({"allEnvComments": allEnvComments, "appUser": appUser.firstName, "comment" : comment}))

app = webapp2.WSGIApplication([
    ('/', LogInPage),
    ('/register', RegisterPage),
    ('/home', HomePage),
    ('/financial', StockPage),
    ('/vote', VotePage),
    ('/environment', EnvironmentPage)
], debug=True)
