from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "high tym to create your key"

# Create a form user function
class NameForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField('Submit')
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

# Create Name Page 
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",name=name,form=form)
