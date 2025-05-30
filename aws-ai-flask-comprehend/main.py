from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

# Initialize AWS Comprehend Client
comprehend = boto3.client('comprehend', region_name='ca-central-1')

@app.route("/", methods=["GET", "POST"])
def index():
    entities = []
    syntax_tokens = []

    if request.method == "POST":
        text = request.form["text"]

        # Named Entity Recognition (NER)
        ner_response = comprehend.detect_entities(Text=text, LanguageCode="en")
        entities = ner_response.get("Entities", [])

        # Part of Speech (PoS) Tagging
        pos_response = comprehend.detect_syntax(Text=text, LanguageCode="en")
        syntax_tokens = pos_response.get("SyntaxTokens", [])

    return render_template("index.html", entities=entities, syntax_tokens=syntax_tokens)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
