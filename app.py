from flask import *
from sqlite3 import *


app = Flask(__name__)


# Redirect to home page
@app.route('/')
def home():
    return render_template("index.html", template_folder="templates")


# Redirect to sign in page
@app.route('/sign-in')
def login():
   return render_template("sign-in.html",template_folder="templates")

# Redirect to sign up page
@app.route('/sign-up')
def sign_up():
   return render_template("sign-up.html",template_folder="templates")
# Redirect to Astronomy chats
@app.route('/astronomy')
def astronomy():
    return render_template("astro.html", template_folder="templates")


# Redirect to Mathematics chats
@app.route('/mathematics')
def mathematics():
   return render_template("math.html", template_folder="templates")

if __name__ == '__main__':
    app.run(debug=True)
