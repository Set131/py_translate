from my_package.first_module import TransLate, LanguageList, CodeLang, LangDetect

def main():
    text = "Hello"
    print(CodeLang(text))
    print(LangDetect("confidence", text))
    print("Translation:", TransLate(text, "en", "fr"))
    print("Language list:")
    print(LanguageList("screen", text))

if __name__ == "__main__":
    main()