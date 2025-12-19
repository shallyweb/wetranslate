languages = {
    "igbo" : {  #by Chiemelie D. Nwosu
    'morning': 'ụtụtụ',
    'fowl': 'ọkụkọ',
    'head': 'isi',
    'university': 'mahadụm',
    'book': 'akwụkwọ',
    'phone': 'ekwenti',
    'teacher': 'onye nkuzi',
    'car': 'ugboala',
    'god': 'chukwu',
    'dog': 'nkịta',
    'fish': 'azụ',
    'hand': 'áká',
    'leg': 'ọkpa',
    'prayer': 'ekpele',
    'food': 'nrị',
    'cloth': 'ákwà',
    'family': 'ezinụlọ',
    'animal': 'anumanu',
    'child': 'nwatakili',
    'thanks': 'daalụ'
     },
    "igala": { #by Adaji Shalom Unekuojo
        'morning': 'odudu',
        'fowl': 'ajuwe',
        'head': 'oji',
        'person': 'one',
        'book': 'otaida',
        'father': 'atah',
        'teacher': 'akuko',
        'car': 'moto',
        'water': 'omi',
        'dog': 'aja',
        'fish': 'ẹja',
        'hand': 'owo',
        'leg': 'ẹsẹ',
        'prayer': 'aduwa',
        'food': 'ounjẹ',
        'cloth': 'ukpo',
        'siblings': 'omaye',
        'house': 'ouni',
        'child': 'ọma',
        'thanks': 'agba'
    },
   "yoruba": {#by Olaniyi Hephzibah Oluwatitomisin
        'morning': 'Ekaaaro',  
        'dog':'aja',
        'wife': 'iyawo',
        'husband':'oko',
        'friend':'ore',
        'man':'okurin',
        'sorry':'ma binu'
        'house':'ile',
        'water':'omi',
        'food':'ounje',
        'money':'owo',
        'day':'ojo',
        'woman':'obirin',
        'no':'rara',
        'yes':'beeni',
        'please':'jowo',
        'goodbye':'o dabo',
        'love':'ife',
        'head':'ori',
        'leg':'ese',
   },
 "hausa": { #by Ezeagu Chioma Peace
     'house': 'gida',
     'door': 'kofa',
     'sheep': 'tunkiya',
     'water': 'ruwa',
     'meat': 'nama',
     'stomach': 'ciki',
     'thank you': 'godiya',
     'money': 'kudi',
     'rice': 'shinkafa',
     'grandfather': 'kaka',
     'grandmother': 'mama',
     'child': 'yaro',
     'husband': 'miji',
     'wife': 'mata',
     'watch': 'kallo',
     'rabbit': 'zumo',
     'hello': 'sannu',
     'fis': 'kifi',
     'rope': 'laya',
    'goodbye': 'sai an jana'
},
}

language = input("Choose a language (Igbo, Igala, Yoruba, Hausa or): ").strip().lower()

if language not in languages:
    print("Sorry, this language is not available.")
else:
    word = input("What word do you want to translate? ").strip().lower()
    translation = languages[language].get(word)

    if translation:
        print(f"Translation ({language.title()}): {translation}")
    else:
        print("Sorry, we do not have the translation of this word.")














