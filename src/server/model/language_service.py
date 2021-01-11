from langdetect import detect, detect_langs
from iso639 import languages


class LanguageDetect:
    """
    service for detecting languages and returning object

    :autor: Benjamin Bulis
    :version: V1.0
    """

    def detect_language(self, input):
        """
        detecting langauge and manage other return parameters

        :param input: input text from controller
        :return: object - reliability, language, short name. probability
        """
        detect_result = detect_langs(input)
        split_result = str(detect_result[0]).split(":")     # spliting string in to array entries


        long_name = languages.get(alpha2=split_result[0]).name      # getting long name of language
        reliable = False if float(split_result[1]) <= 0.8 else True        # setting reliability
        short_name = split_result[0]
        prob = split_result[1]

        return {"reliable": reliable, 'language': long_name, 'short': short_name, "prob": prob}

