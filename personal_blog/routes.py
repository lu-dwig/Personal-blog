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