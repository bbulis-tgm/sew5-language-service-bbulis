class HtmlFormatter:

    def formatter(self, json):
        """
        gets json object and returns html string fot printing to output-field

        :param json: json object which is used for formating
        :return ret: html string for printing to output field
        """
        reliable = json['result'][0]
        language = json['result'][1]
        short = json['result'][2]
        prob = json['result'][3]

        ret = "reliable: " + "<b>yes</b>" if reliable else "<b>no</b>"
        ret += "<br>language: <b>" + str(language) + "</b>"
        ret += "<br>probability: <b>" + "{:.2f}".format(prob) + "</b>"

        return ret
