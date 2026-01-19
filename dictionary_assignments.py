languages = {
    "igbo" : {  #by Chiemelie Daniel Nwosu
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
        'sorry':'ma binu',
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
        'leg':'ese'
   },
 "hausa": { #by Ezeagu Chioma Peace
     'house': 'gida',
     'door': 'kofa',
     'sheep': 'tunkiya',
     'water': 'ruwa',
     'meat': 'nama',
     'stomach': 'ciki',
     'thanks': 'godiya',
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
     'fish': 'kifi',
     'rope': 'laya',
    'goodbye': 'sai an jana'
},
    "idoma": {# by Okpe 0yigocho Michelle
  
        'fowl':'ougou',
        'leg': 'igpo',
        'book': 'ookpa',
        'good': 'olohi',
        'uncle': 'atahhue',
        'school': 'eopka',
        'car': 'moto',
        'water': 'enkpo',
        'cat': 'busse',
        'plate': 'ogo',
        'phone': 'odo baho',
        'fingers': 'apin kpo',
        'prayer': 'aduwa',
        'food': 'odree',
        'shoe': 'adaba',
        'sister': 'oine',
        'building': 'ole',
        'glasses': 'odo baye',
        'bag': 'ekpatii',
        'light':'ola'
},
}

def main():

    language = st.selectbox("Choose a Language:", ["Igbo", "Igala", 'Yoruba', "Hausa", "Idoma"]).lower()
    st.title("Nigerian Language Translator")
    st.write(f" Convert from English to {language}")

    word = st.text_input(f" What English word do you want to translate to {language}").strip().lower()

    if st.button("Translate"):

        if language not in languages:
            st.error("Sorry, this language is not available")

        else:
            if word == "":
                st.warning("Please enter your English word")

            else:
                translation = languages[language].get(word)

                if translation:
                    st.success(f" Translation {language.title()}: {translation}")

                else:
                    st.error(f" Sorry, we do not have the {language} translation of this word")

if __name__ == "__main__":
    main()




















