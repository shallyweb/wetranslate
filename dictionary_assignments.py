igbo_dict = {  #by Chiemelie D. Nwosu
    'morning': 'ututu',
    'fowl': 'okuko',
    'head': 'isi',
    'university': 'mahadum',
    'book': 'akwukwo',
    'phone': 'ekwenti',
    'teacher': 'onye nkuzi',
    'car': 'ugboala',
    'god': 'chukwu',
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
    'thanks': 'daalu'
}
key = input('what do you want to tranlate? ').lower()
if key in igbo_dict:
    print(igbo_dict[key])
else:
    print('Sorry, I do not have the translation of this word')



