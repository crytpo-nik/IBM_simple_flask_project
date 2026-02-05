from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def rend_indec_page():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
