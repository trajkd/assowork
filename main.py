import getClientMAC

import os

import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

import re
def valid_username(username):
	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	return username and USER_RE.match(username)

def valid_password(password):
	PASS_RE = re.compile(r"^.{3,20}$")
	return password and PASS_RE.match(password)

def valid_email(email):
	EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
	return not email or EMAIL_RE.match(email)

import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    ###Your code here
    if make_pw_hash(name, pw, h.split(",")[1]) == h:
        return True

class RecupHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(jinja_env.get_template('recup.html').render())

class MACAddressHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(jinja_env.get_template('macaddress.html').render())

def render_str(template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	def render_str(self, template, **params):
		return render_str(template, **params)
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class GetClientMACHandler(Handler):
	def post(self):
		return getClientMac()

class LoginHandler(Handler):
	def get(self):
		self.render("login.html")

import mimetypes
class StaticFileHandler(webapp2.RequestHandler):
    def get(self, path):
        abs_path = os.path.abspath(os.path.join(self.app.config.get('webapp2_static.static_file_path', 'static'), path))
        if os.path.isdir(abs_path) or abs_path.find(os.getcwd()) != 0:
            self.response.set_status(403)
            return
        try:
            f = open(abs_path, 'r')
            self.response.headers.add_header('Content-Type', mimetypes.guess_type(abs_path)[0])
            self.response.headers['Content-Type'] = mimetypes.guess_type(abs_path)[0]
            self.response.out.write(f.read())
            f.close()
        except:
            self.response.set_status(404)

app = webapp2.WSGIApplication([
	('/', LoginHandler),
	('/login', LoginHandler),
	('/Home/ShowRecup', RecupHandler),
	('/mac', GetClientMACHandler),
    (r'/static/(.+)', StaticFileHandler)
], debug = True)

def main():
    from paste import httpserver

    httpserver.serve(app, host='172.31.10.39', port='80')

if __name__ == '__main__':
    main()