
from window import ROOT

def rotate_language(selected_language, language_string_var, status_bar_label):
    supported_languages = ROOT["language"]["supported"]
    selected_language["name"] = selected_language["name"] + 1 if selected_language["name"] < len(supported_languages) - 1 else 0

    language = supported_languages[selected_language["name"]]
    language_string_var.set(language)
    status_bar_label.config(text=f"Language set to {language}")