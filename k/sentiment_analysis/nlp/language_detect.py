import logging
from googletrans import Translator

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

translator=Translator()
logger.info("Translation service instance created sucessfully")

class Langtranslator:
    
    def text_translate(self, input_text):
        

    # Detect and translate the text to English
        translation_result = translator.translate(input_text, dest='en')  
        self.lang = translation_result.src  # store detected language
    
        if self.lang == 'en':
                logger.info("Detected language is English, no need to translate.")
                self.translated = input_text  # no translation needed
        else:
                logger.info(f"The detected language is {self.lang}, translating to English.....")
                self.translated = translation_result.text  # get translated text correctly
                logger.info(f"The translated text is:{self.translated}")
    
        return self.translated

langtranslator=Langtranslator()



