from my_package.second_module import TransLate, LangDetect, CodeLang, LanguageList

def main():
    text = "My holiday"
    print("Translation:", TransLate(text, "en", "fr"))
    print("Detected language:", LangDetect(text, "lang"))
    print("Confidence:", LangDetect(text, "confidence"))
    print("Language code:", CodeLang("English"))
    print("Language list:")
    LanguageList("screen", text)

if __name__ == "__main__":
    main()