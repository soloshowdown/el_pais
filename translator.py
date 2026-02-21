from googletrans import Translator

translator = Translator()


def translate_text(text):
    try:
        translated = translator.translate(text, src="es", dest="en")
        return translated.text
    except Exception:
        return text