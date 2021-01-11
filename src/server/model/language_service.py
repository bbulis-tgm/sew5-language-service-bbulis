from langdetect import detect
from iso639 import languages


class LanguageDetect:

    def detect_language(self, input):
        short_name = detect(input)
        long_name = languages.get(alpha2=short_name).name
        return {'language': long_name, 'short': short_name}
