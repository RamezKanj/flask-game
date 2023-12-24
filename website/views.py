from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from . import db
from .models import Game

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/adventure')
@login_required
def adventure():
    return render_template("adventure.html", user=current_user)

@views.route('/credits')
def credits():
    return render_template("credits.html", user=current_user)

@views.route('/feedback')
def feedback():
    return render_template("feedback.html", user=current_user)

@views.route('/donate')
def donate():
    return render_template("donate.html", user=current_user)
