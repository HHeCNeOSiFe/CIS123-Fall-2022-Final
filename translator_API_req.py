from googletrans import Translator, LANGUAGES
import random

translator = Translator()

def get_language():
    '''The intro has a line that the language this function returns is NOT
       a language they have heard, so this randomizes and "rerolls" the value
       if/when it happens to choose English, under the assumption that anyone
       trying it out likely speaks English.'''
    while 'language is not English':  # Haha, truthiness is great
        lang = str(random.choice(list(LANGUAGES.keys())))
        if lang == 'en':
            continue
        else:
            return lang

lang = get_language()
def intro_translator_API_call(text):
    global lang
    return translator.translate(text, lang).text