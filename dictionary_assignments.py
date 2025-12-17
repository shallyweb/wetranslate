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
        'morning': 'ojale',
        'fowl': 'ẹnyẹ',
        'head': 'oju',
        'university': 'ile-ẹkọ giga',
        'book': 'iwe',
        'phone': 'tẹlifoonu',
        'teacher': 'akuko',
        'car': 'moto',
        'god': 'Ojochamachala',
        'dog': 'aja',
        'fish': 'ẹja',
        'hand': 'owo',
        'leg': 'ẹsẹ',
        'prayer': 'adura',
        'food': 'ounjẹ',
        'cloth': 'aso',
        'family': 'ebi',
        'animal': 'ẹranko',
        'child': 'ọmọ',
        'thanks': 'agba'
    }
}

language = input("Choose a language (Igbo or Igala): ").strip().lower()

if language not in languages:
    print("Sorry, this language is not available.")
else:
    word = input("What word do you want to translate? ").strip().lower()
    translation = languages[language].get(word)

    if translation:
        print(f"Translation ({language.title()}): {translation}")
    else:
        print("Sorry, we do not have the translation of this word.")








