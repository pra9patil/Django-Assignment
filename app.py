from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    language = request.args.get('language', 'English').lower()
    if language == 'english':
        return "Hello world"
    elif language == 'french':
        return "Bonjour le monde"
    elif language == 'hindi':
        return "Namastey sansar"
    else:
        return "Language not supported", 400

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
