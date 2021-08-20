from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
        return "hello flask-heroku"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/name')
def name():
        return "<font color=purple>เจนจิราพร ทองแดง</font> <br>เลขที่ 10 ม.4/10"

@app.route('/hello/<string:name>')
def Home(name):
	return render_template('home.html', name_html=name)

if __name__ == "__main__":
    app.run(debug=False)
