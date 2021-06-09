from flask import Flask, request, jsonify
from dailyhunt import getNews
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "HELLO_WORLD"
CORS(app)


@app.route('/')
def index():
    return "API is UP and running"


@app.route('/categories')
def categories():
    return "<p>science</p>"\
        "<p>technology</p>"\
        "<p>india</p>"\
        "<p>automobile</p>"\
        "<p>entertainment</p>"\
        "<p>sports</p>"\
        "<p>world</p>"\
        "<p>lifestyle</p>"\
        "<p>employment</p>"\
        "<p>religion</p>"\
        "<p>football</p>"\
        "<p>movie</p>"


@app.route('/languages')
def languages():
    return "<p>english</p>"\
        "<p>hindi</p>"\
        "<p>marathi</p>"\
        "<p>gujarati</p>"\
        "<p>punjabi</p>"\
        "<p>bangla</p>"\
        "<p>kannada</p>"\
        "<p>tamil</p>"\
        "<p>telugu</p>"\
        "<p>malayalam</p>"\
        "<p>oriya</p>"\
        "<p>urdu</p>"\
        "<p>bhojpuri</p>"\
        "<p>nepali</p>"

@app.route('/dailyhunt')
def news():
    if request.method == 'GET':
        category = request.args.get('category')
        language = request.args.get('language')
        items = request.args.get('items')
        return jsonify(getNews(language, category, items))


if __name__ == '__main__':
    app.run(debug=True)
