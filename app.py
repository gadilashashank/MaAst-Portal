from flask import *
from sqlite3 import *


app = Flask(__name__)


# Redirect to home page
@app.route('/')
def home():
    return render_template("index.html", template_folder="templates")


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
