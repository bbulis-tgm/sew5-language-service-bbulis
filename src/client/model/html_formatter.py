class HtmlFormatter:

    def formatter(self, json):
        """
        gets json object and returns html string fot printing to output-field

        :param json: json object which is used for formating
        :return ret: html string for printing to output field
        """
        print(json)
        reliable = json['result']['reliable']
        language = json['result']['language']
        short = json['result']['short']
        prob = json['result']['prob']
        prob_out = round(float(prob)*100,2)

        ret = "reliable: " + "<b>yes</b>" if reliable else "<b>no</b>"
        ret += "<br>language: <b>" + str(language) + "</b>"
        ret += "<br>probability: <b>" + str(prob_out) + "</b>"

        return ret
