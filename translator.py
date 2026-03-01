
from googletrans import Translator
from logger import logger

translator = Translator()


def translate_text(text):
    try:
        logger.info(f"Translating text: {text}")
        translated = translator.translate(text, src="es", dest="en")
        return translated.text
    except Exception as e:
        logger.error(f"Translation failed: {e}")
        return text