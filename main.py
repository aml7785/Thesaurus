import json
from spellchecker import SpellChecker

data = json.load(open("data.json"))
spell = SpellChecker()
def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif spell.correction(word) in data:
            result = input(f'Did you mean to put ' + spell.correction(word) + '? Y or N')
            if result == 'Y':
                return data[spell.correction(word)]
            elif result == 'N':
                return 'Sorry I can\'t find that word'
            else:
                return 'We didn\'t understand that response.'
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)

