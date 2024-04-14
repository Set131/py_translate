from googletrans import Translator

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str) -> str:
    try:
        translator = Translator()
        detected_lang = translator.detect(text)
        if set == "lang":
            return detected_lang.lang
        elif set == "confidence":
            return str(detected_lang.confidence)
        else:
            return f"Language: {detected_lang.lang}, Confidence: {detected_lang.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    try:
        translator = Translator()
        detected_lang = translator.translate(lang, dest='en').src
        return detected_lang
    except Exception as e:
        return str(e)

def LanguageList(out: str, text: str = None) -> str:
    try:
        translator = Translator()
        
        # Список мов, на які будемо перекладати
        languages = ["en", "es", "de", "it", "pt", "ru", "zh-CN", "ja", "ko", "ar"]
        
        # Отримання перекладів фрази на кожну з мов
        translations = []
        for lang_code in languages:
            translation = translator.translate(text, dest=lang_code).text
            translations.append((lang_code, translation))

        # Створення словника з кодів мов та відповідних назв країн на англійській
        country_names = {
            "en": "English",
            "es": "Spanish",
            "de": "German",
            "it": "Italian",
            "pt": "Portug.",
            "ru": "Russian",
            "zh-CN": "Chinese",
            "ja": "Japan.",
            "ko": "Korean",
            "ar": "Arabic"
        }

        # Форматування результатів для виведення
        if out == "screen":
            output = "N\tLanguage\tISO-639 code\tText\n" + "-" * 50 + "\n"
            for index, (lang_code, translated_text) in enumerate(translations, start=1):
                lang_name = country_names.get(lang_code, "Unknown")
                output += f"{index}\t{lang_name}\t\t{lang_code}\t\t{translated_text}\n"
            return output
        else:
            return "Invalid output option. Please specify 'screen' or 'file'."
    except Exception as e:
        return str(e)