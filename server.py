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
    text_result = format_emotion_result(result)

    return text_result

def format_emotion_result(result):
    # Extract the dominant emotion
    dominant = result.get("dominant_emotion")

    # Remove 'dominant_emotion' from dict so we only have the numeric values
    values_dict = {k: v for k, v in result.items() if k != "dominant_emotion"}

    # Get all keys except the last one
    keys = list(values_dict.keys())
    last_key = keys[-1]
    other_keys = keys[:-1]

    # Build the first part: " 'anger': 0.006, ... and 'sadness': 0.049 "
    parts = []
    for k in other_keys:
        parts.append(f"'{k}': {values_dict[k]}")
    # Add last key with "and"
    parts.append(f"and '{last_key}': {values_dict[last_key]}")

    # Join with commas
    first_sentence = ", ".join(parts)

    # Final string
    formatted = f"For the given statement, the system response is {first_sentence}. The dominant emotion is {dominant}."

    return formatted

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
