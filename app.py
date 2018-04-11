from flask import *
from sqlite3 import *
import model

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html',template_folder='templates')

@app.route('/login' , methods=['POST','GET'])
def login():
    error = None
    if request.method is 'POST':
        if request.form['username'] != 'admin' and request.form['password'] != 'admin':
            error = 'Invalid creds'
        else:
            return redirect(url_for('home'))
    return render_template('sign_in.html', error=error,template_folder='templates')


if __name__ == '__main__':
    app.run(debug=True)
