from my_package.first_module import TransLate
import os

def read_config(config_file: str) -> dict:
    """
    Function to read configuration data from config file.
    """
    config = {}
    with open(config_file, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split(":")
            config[key.strip()] = value.strip()
    return config

def requirments(file_path: str, source_lang: str, target_lang: str, config_file: str) -> None:
    try:
        config = read_config(config_file)
        
        output_destination = config.get("Output destination")
        max_characters = int(config.get("Max characters"))
        max_words = int(config.get("Max words"))
        max_sentences = int(config.get("Max sentences"))
        
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            translated_text = TransLate(text, source_lang, target_lang)

        print("\n_________________________________________________________________\n")
        print(f"Загальна кількість символів у файлі: {len(text)}")
        print(f"Кількість речень у файлі: {text.count('.')}")
        print(f"Загальна кількість символів у файлі: {text.count(' ')}")
        
        if output_destination == "screen":
            print("_________________________________________________________________\n")
            print(f"Translation: {translated_text}")
        elif output_destination == "file":
            print("Розмір файлу :", round(os.path.getsize("requirments.txt")/1024, 3),"Kb")
            print("_________________________________________________________________\n")
            with open("requirments.txt", "w", encoding="utf-8") as requirments:
                requirments.write(translated_text)
            print("Translation saved to 'requirments.txt'")
        else:
            print("Invalid output destination specified in config file.")
    except Exception as e:
        print("An error occurred:", str(e))

requirments("C:/Users/USER/Documents/python_for_me/Geroiev/input.txt", "uk", "fr", "C:/Users/USER/Documents/python_for_me/Geroiev/config.txt")