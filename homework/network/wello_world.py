from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello world!'


app.run(host='0.0.0.0', port=5055, debug=True)
