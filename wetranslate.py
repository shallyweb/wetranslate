
languages = {
    "igbo": { #by Chiemelie D. Nwosu
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
    },
    "igala": { #by Adaji Shalom Unekuojo
        'morning': 'ojale',
        'fowl': 'ẹnyẹ',
        'head': 'oju',
        'university': 'ile-ẹkọ giga',
        'book': 'iwe',
        'phone': 'tẹlifoonu',
        'teacher': 'ọkọ́ni',
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
        'thanks': 'oche'
    }
}


language = input("Choose a language (Igbo or Igala): ").lower()

if language not in languages:
    print("Sorry, this language is not available.")
else:
    word = input("What word do you want to translate? ").lower()
    translation = languages[language].get(word)

    if translation:
        print(f"Translation ({language.title()}): {translation}")
    else:
        print("Sorry, we do not have the translation of this word.")