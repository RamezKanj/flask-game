from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from website.logic.letterMap import get_random_key, get_random_value, incorrect_keys
from . import db
from .models import Game

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/get_random_data', methods=['GET'])
@login_required
def get_random_data():
    random_key = get_random_key()
    random_value = get_random_value(random_key)
    incorrect_key_one, incorrect_key_two = incorrect_keys(random_key)


    return jsonify({
        'random_key': random_key,
        'random_value': random_value,
        'incorrect_key_one': incorrect_key_one,
        'incorrect_key_two': incorrect_key_two,
    })

@views.route('/update_score', methods=['POST'])
@login_required
def update_score():
    try:
        score = int(request.form.get('score'))
        game = Game(score=score, user_id=current_user.id)
        db.session.add(game)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Score updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})