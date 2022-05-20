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

