class HtmlFormatter:

    def __init__(self, json):
        """
        gets json object and returns html string fot printing to output-field

        :param json:
        """
        reliable = json['result'][0]
        language = json['result'][1]
        short = json['result'][2]
        prob = json['result'][3]