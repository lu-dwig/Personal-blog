import os
import json
import requests
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from personal_blog import app, db, bcrypt
from personal_blog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm
from personal_blog.models import User, Post, Comment, Quote
from flask_login import login_user, current_user, logout_user, login_required


def get_quote():
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    req = requests.get(quote_url)
    data = json.loads(req.content)
    quote = Quote(data["quote"],data["author"])
    return quote

@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    quote = get_quote()
    return render_template('home.html', posts=posts, quote=quote)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit() 
        flash('Your account has been created You can log in now!', 'success')
        return redirect(url_for('login'))  
    return render_template('register.html', title='Register', form=form)
