"""
view the v in the mvc

"""
# views.py

from flask import render_template, url_for, redirect, request

from app import app
data = {}
app.secret_key = "silasomurunga"

#inddex route
@app.route('/', methods=['GET'])
def index():
    """index route/ about page"""
    return render_template("index.html")

#about route
@app.route('/about', methods=['GET'])
def about():
    """about route /about page"""
    message = {
        "titles":"welcome to business",
        "description":"This is a good venture"
    }
    return render_template("about.html", message=message)

#signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """signnup route register page"""
    return render_template('register.html')

#store route
@app.route('/store', methods=['POST'])
def store():
    """store route about page"""
    if request.method == 'post':
        username = request.form['username']
        fname = request.form['Fname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        data.update({username:[username, fname, lastname, email, password, cpassword]})
    return redirect(url_for('login'))

#login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    """login route/login page"""
    return render_template('login.html')


#logout route
@app.route('/logout')
def logout():
    """about route about page"""
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
