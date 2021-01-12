import requests


class LanguageRequest:
    """
    Using the language-detection server

    :author: Benjamin Bulis
    :version: V1.0
    """

    base_url = "http://127.0.0.1:5000"

    def language(self, input):
        """
        methode connects to language detection service and gets reseults

        :param input: text from the user input
        :return: the response from the detection service
        :raise: raises exception if no connection to language service is possible
        """
        params = {"id": input}
        try:
            response = requests.get(self.base_url + "/lg", params=params)
        except Exception as e:
            print(e)
            raise Exception("Not able to connect to language detection service")
        response_json = response.json()
        if not response_json['success']:
            raise Exception("An Error occured")
        return response_json
