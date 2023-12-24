from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from . import db
from .models import Game
import random

lingo = Blueprint('lingo', __name__)


@lingo.route('/lingo', methods=['GET', 'POST'])
@login_required
def game():
    return render_template("lingo.html", user=current_user)


@lingo.route('/get_random_data', methods=['GET'])
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


@lingo.route('/update_score', methods=['POST'])
@login_required
def update_score():
    try:
        score = int(request.form.get('score'))
        time = int(request.form.get('time_control'))
        game = Game(score=score, time=time, user_id=current_user.id)
        db.session.add(game)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Score updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


#Dictionary that stores arabic transliterations in English letters as keys
#with the actual arabic letter as a value in its different forms

letter_map = {
    "alif": ["ا", "ـا", "آ", "إ", "أ"],
    "Ba": ["ب", "بـ", "ـبـ", "ـب"],
    "Ta": ["ت", "تـ", "ـتـ", "ـت"],
    "Tha": ["ث", "ثـ", "ـثـ", "ـث"],
    "Jim": ["ج", "جـ", "ـجـ", "ـج"],
    "Hha": ["ح", "حـ", "ـحـ", "ـح"],
    "Kha": ["خ", "خـ", "ـخـ", "ـخ"],
    "Dal": ["د", "ـد", "ـد", "د"],
    "Dhal": ["ذ", "ـذ", "ـذ", "ذ"],
    "Ra": ["ر", "ـر", "ـر", "ر"],
    "Zay": ["ز", "ـز", "ـز", "ز"],
    "Sin": ["س", "سـ", "ـسـ", "ـس"],
    "Shin": ["ش", "شـ", "ـشـ", "ـش"],
    "Sad": ["ص", "صـ", "ـصـ", "ـص"],
    "Dad": ["ض", "ضـ", "ـضـ", "ـض"],
    "Tah": ["ط", "طـ", "ـطـ", "ـط"],
    "Zah": ["ظ", "ظـ", "ـظـ", "ـظ"],
    "ayn": ["ع", "عـ", "ـعـ", "ـع"],
    "Ghayn": ["غ", "غـ", "ـغـ", "ـغ"],
    "Fa": ["ف", "فـ", "ـفـ", "ـف"],
    "Qaf": ["ق", "قـ", "ـقـ", "ـق"],
    "Kaf": ["ك", "كـ", "ـكـ", "ـك"],
    "Lam": ["ل", "لـ", "ـلـ", "ـل"],
    "Mim": ["م", "مـ", "ـمـ", "ـم"],
    "Ha": ["ه", "هـ", "ـهـ", "ـه"],
    "Waw": ["و", "ـو", "ـو", "و"],
    "Ya": ["ي", "يـ", "ـيـ", "ـي"],
    "Hamza": ["ء", "ء", "ء", "ء"],
}

#Return a random key from letter map

def get_random_key():
    random_key = random.choice(list(letter_map.keys()))
    return random_key

#Return a random value from a specified key

def get_random_value(key):
    return random.choice(letter_map[key])


#Return two keys ('incorrect keys') different than the given key in the map
#e.g. incorrect_keys("hamza") -> any two other keys in the map that is not hamza

def incorrect_keys(key):
    
    if key not in letter_map:
        return None

    all_keys = list(letter_map.keys())

    all_keys.remove(key)

    incorrect_key_one = random.choice(all_keys)

    incorrect_key_two = random.choice(all_keys)

    while incorrect_key_two == incorrect_key_one:
        incorrect_key_two = random.choice(all_keys)
    
    return incorrect_key_one, incorrect_key_two