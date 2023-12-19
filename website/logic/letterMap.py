import random

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

def get_random_key():
    random_key = random.choice(list(letter_map.keys()))
    return random_key

def get_random_value(key):
    return random.choice(letter_map[key])

def incorrect_values(key):
    if key not in letter_map:
        return None
    
    correct_values = letter_map[key]

    all_values = [value for values in letter_map.values() for value in values]

    incorrect_values = [value for value in all_values if value not in correct_values]

    random_incorrect_value_one = random.choice(list(incorrect_values))

    random_incorrect_value_two = random.choice(list(incorrect_values))
    while random_incorrect_value_two == random_incorrect_value_one:
        random_incorrect_value_two = random.choice(list(incorrect_values))

    return random_incorrect_value_one, random_incorrect_value_two


