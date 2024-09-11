from flask import Flask, request, jsonify, render_template, url_for

application = Flask(__name__)

@application.route('/hello', methods=['GET'])
def hello_world():
    language = request.args.get('language', 'English').lower()
    if language == 'english':
        response = {
            "greeting": "Hello world",
            "backgroundImage": url_for('static', filename='english.png')
        }
    elif language == 'french':
        response = {
            "greeting": "Bonjour le monde",
            "backgroundImage": url_for('static', filename='french.png')
        }
    elif language == 'hindi':
        response = {
            "greeting": "Namastey sansar",
            "backgroundImage": url_for('static', filename='hindi.png')
        }
    else:
        response = {
            "greeting": "Language not supported",
            "backgroundImage": url_for('static', filename='default_bg.png')
        }

    return jsonify(response)

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
