# views.py

from flask import render_template, url_for, redirect

from app import app

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/about', methods = ['GET'])
def about():
    message = {
        "titles":"welcome to business",
        "description":"This is a good venture"
    }
    return render_template("about.html", message = message )

@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
