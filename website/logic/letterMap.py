import random


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