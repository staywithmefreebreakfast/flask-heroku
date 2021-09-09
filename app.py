from flask import Flask, jsonify
from flask import Flask, render_template, Response 
import cv2

camera = cv2.VideoCapture('rtsp://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream')

app = Flask(__name__)

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
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
