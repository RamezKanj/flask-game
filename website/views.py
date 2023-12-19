from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from website.logic.letterMap import get_random_key, get_random_value, incorrect_keys


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/get_random_data', methods=['GET'])
def get_random_data():
    # Get a new set of random data
    random_key = get_random_key()
    random_value = get_random_value(random_key)
    incorrect_key_one, incorrect_key_two = incorrect_keys(random_key)

    # Return the data as JSON
    return jsonify({
        'random_key': random_key,
        'random_value': random_value,
        'incorrect_key_one': incorrect_key_one,
        'incorrect_key_two': incorrect_key_two
    })