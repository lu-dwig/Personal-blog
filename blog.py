from flask import Flask, render_template


# Create a flask instance
app = Flask(__name__)

# Create routes
@app.route('/')

def index():
    full_name ="Ludwig Murimi"
    stuff = "coding is one of my greatest passion"
    
    return render_template("index.html", full_name=full_name, stuff=stuff)

# Create user blog
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

# Create Custom Error Pages

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(error):
    return render_template("404.html", error=error), 404 
    