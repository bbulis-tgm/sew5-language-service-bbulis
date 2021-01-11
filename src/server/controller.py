from flask import Flask, request, jsonify
from model.language_service import LanguageDetect

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False    # stop sorting keys for returning
language = LanguageDetect()

"""
Server for detecting languages

:author: Benjamin Bulis
:version: V1.0
"""


@app.route('/lg')   # defining route for server app
def hello():
    """
    Detecting the given languages and returning an JSON object
    returning error message if no input is given

    :return: return json object with requestet data
    """
    id = request.args.get("id")  # getting argument from url
    if id is None:
        return jsonify({"success": False, "error": "no parameter id given"})
    if id == "":
        return jsonify({"success": False, "error": "no text given"})
    result = language.detect_language(id)
    return jsonify({"success": True, "result": result})


if __name__ == '__main__':
    app.run(debug=False)
