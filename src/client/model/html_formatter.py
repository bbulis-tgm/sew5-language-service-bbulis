class HtmlFormatter:
    """
    HtmlFormatter gets output and return HTML String

    :author: Benjamin Bulis
    :version: V1.0
    """

    def formatter(self, json):
        """
        gets json object and returns html string fot printing to output-field

        :param json: json object which is used for formating
        :return ret: html string for printing to output field
        """
        print(json)     # printing Json Object for Checking
        reliable = json['result']['reliable']
        language = json['result']['language']
        short = json['result']['short']
        prob = json['result']['prob']
        prob_out = round(float(prob)*100,2)     # Return value between 0 and 1 - multiply with 100 and rounding to two digits

        # building return html string
        ret = "reliable: " + "<b>yes</b>" if reliable else "<b>no</b>"
        ret += "<br>language: <b>" + str(language) + "</b>"
        ret += "<br>probability: <b>" + str(prob_out) + "</b>"

        return ret
