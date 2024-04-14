from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translated_text = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str) -> str:
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return str(GoogleTranslator(source='auto', target='en').translate(text))
        else:
            return f"Language: {detected_lang}, Confidence: {GoogleTranslator(source='auto', target='en').translate(text)}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    try:
        detected_lang = detect(lang)
        if detected_lang:
            return detected_lang
        else:
            return GoogleTranslator(source='auto', target='en').translate(lang)
    except Exception as e:
        return str(e)

def LanguageList(out: str, text: str = None) -> str:
    try:
        translator = GoogleTranslator(source='auto', target='en')
        languages = translator.get_supported_languages(as_dict=True)
        if out == "screen":
            output = "N\tLanguage\tISO-639 code\tText\n" + "-" * 50 + "\n"
            for index, (lang_code, lang_name) in enumerate(languages.items(), start=1):
                translation = GoogleTranslator(source='auto', target=lang_name).translate(text) if GoogleTranslator(source='auto', target=lang_name).translate(text) != text else ""
                if (translation != "" or translation !=  text + "" or translation != "\t" or translation != None):
                    output += f"{index}\t{lang_name}\t{lang_code}\t\t{translation}\n"
            print(output)
            return "Ok"
        else:
            return "Invalid output option. Please specify 'screen' or 'file'."
    except Exception as e:
        return str(e)