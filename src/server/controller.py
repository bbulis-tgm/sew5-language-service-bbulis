from flask import Flask, request, jsonify
from model.language_service import LanguageDetect

app = Flask(__name__)
language = LanguageDetect()


@app.route('/lg')
def hello():
    id = request.args.get("id")
    if id == "":
        return jsonify({"success": "false", "error": "no text given"})
    result = language.detect_language(id)
    return jsonify({"success": True, "result": result})


if __name__ == '__main__':
    app.run(debug=False)
