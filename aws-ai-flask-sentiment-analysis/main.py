from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Initialize AWS Comprehend
comprehend = boto3.client("comprehend", region_name="ca-central-1")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None

    if request.method == "POST":
        text = request.form["text"]
        if text:
            response = comprehend.detect_sentiment(Text=text, LanguageCode="en")
            sentiment_result = response["SentimentScore"]

    return render_template("index.html", sentiment=sentiment_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
