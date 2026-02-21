from googletrans import Translator
import logging

logger = logging.getLogger(__name__)

translator = Translator()

def translate_text(text, src="es", dest="en"):
    try:
        translated = translator.translate(text, src=src, dest=dest)
        logger.info(f"Translated: {text} -> {translated.text}")
        return translated.text
    except Exception as e:
        logger.error(f"Translation failed for {text}: {e}")
        return text