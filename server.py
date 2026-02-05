from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def rend_index_page():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])

def detect_emotion():

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "No text provided", 400

    result = emotion_detector(text_to_analyze)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
