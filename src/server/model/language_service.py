from langdetect import detect, detect_langs
from iso639 import languages


class LanguageDetect:

    def detect_language(self, input):
        detect_result = detect_langs(input)
        split_result = str(detect_result[0]).split(":")


        long_name = languages.get(alpha2=split_result[0]).name
        reliablie = False if float(split_result[1]) <= 0.8 else True
        short_name = split_result[0]
        prob = split_result[1]

        return {'language': long_name, 'short': short_name, "prob": prob, "reliable": reliablie}

