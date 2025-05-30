from flask import Flask, render_template, request
import boto3
import uuid
import time
import json
import requests

app = Flask(__name__)

# AWS Configuration
s3_bucket = "my-ai-input-ca-central"  # Change this to your actual S3 bucket name
aws_region = "ca-central-1"

# AWS Transcribe Client
transcribe = boto3.client("transcribe", region_name=aws_region)

@app.route("/", methods=["GET", "POST"])
def index():
    transcription_text = None  # Variable to store the transcribed text

    if request.method == "POST":
        filename = request.form.get("filename", "").strip()

        if not filename:
            return "Error: Please provide a valid S3 filename.", 400  # Handle missing input

        file_uri = f"s3://{s3_bucket}/{filename}"  # Construct S3 file path
        job_name = f"TranscriptionJob-{uuid.uuid4()}"  # Unique job name

        # Start Transcription Job
        try:
            transcribe.start_transcription_job(
                TranscriptionJobName=job_name,
                Media={"MediaFileUri": file_uri},
                MediaFormat="mp3",
                LanguageCode="en-US"
            )

            # Wait for the transcription job to complete
            while True:
                status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
                if status["TranscriptionJob"]["TranscriptionJobStatus"] in ["COMPLETED", "FAILED"]:
                    break
                time.sleep(5)  # Wait before checking again

            if status["TranscriptionJob"]["TranscriptionJobStatus"] == "COMPLETED":
                transcript_url = status["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]

                # Fetch the transcription result from AWS
                response = requests.get(transcript_url)
                transcript_data = response.json()
                transcription_text = transcript_data["results"]["transcripts"][0]["transcript"]

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("index.html", transcription=transcription_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
