
"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def detector():
    """Analyze the emotion of text provided by the user."""
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)
    emotions = result["Emotions"]
    dominant = result["Dominant"]

    if dominant is None:
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {dominant}."
    )


@app.route("/")
def render_index_page():
    """Render the application's main page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

