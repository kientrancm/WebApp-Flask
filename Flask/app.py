#we import Flask
from flask import Flask, render_template

# We create a Flask app
app = Flask(__name__)

# We establish a Flask route so that we can serve HTTP traffic on that route
@app.route('/')
def cpanel():
    return render_template("index.html")

@app.route('/login')
def dangnhap():
    return "Login Page"


@app.route('/register')
def dangky():
    return "Dang Ky Page"


# Get setup so that if we call the app directly 

if __name__ == '__main__':
    app.run()