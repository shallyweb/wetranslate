igbo_dict = {  #by Chiemelie D. Nwosu
    'morning': 'ututu',
    'fowl': 'okuko',
    'head': 'isi',
    'university': 'mahadum',
    'book': 'akwukwo',
    'phone': 'ekwenti',
    'teacher': 'onye nkuzi',
    'car': 'ugboala',
    'God': 'chukwu',
    'dog': 'nkita',
    'fish': 'azu',
    'hand': 'aka',
    'leg': 'okpa',
    'prayer': 'ekpele',
    'food': 'nri',
    'cloth': 'akwa',
    'family': 'ezinulo',
    'animal': 'anumanu',
    'child': 'nwatakili',
    'Thanks': 'daalu'
}
def translate(word):
    word = word.lower()
    if word in igbo_dict:
        return igbo_dict[word]
    else:
        return "Oops! Seems like we do not have the translation of this word"

key = input('What do you want to translate? ')
print(translate(key))

