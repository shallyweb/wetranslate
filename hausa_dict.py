english_dict = {
    "house": "gida",
    "door": "kofa",
    "sheep": "tunkiya",
    "water": "ruwa",
    "meat": "nama",
    "stomach": "ciki",
    "thank you": "godiya",
    "money": "kudi",
    "rice": "shinkafa",
    "grandfather": "kaka",
    "grandmother": "mama",
    "child": "yaro",
    "husband": "miji",
    "wife": "mata",
    "watch": "kallo",
    "rabbit": "zumo",
    "hello": "sannu",
    "fish": "kifi",
    "rope": "laya",
    "goodbye": "sai an jana",
}
def translate_to_hausa(word):
    return english_dict.get(word.lower(), "Not found in dictionary.")
def main():
    print("English to Hausa Dictionary")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter an English word: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        translation = translate_to_hausa(user_input)
        print(f" {user_input} -> **{translation}**\n ")

if __name__ == "__main__":
    main()