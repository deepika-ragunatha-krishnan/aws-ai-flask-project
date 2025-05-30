from flask import Flask, render_template, request
import boto3
import uuid

app = Flask(__name__)

# AWS Configuration
s3_bucket = "my-ai-input-ca-central"  # Change this to your actual S3 bucket name
aws_region = "ca-central-1"

# AWS Transcribe Client
transcribe = boto3.client("transcribe", region_name=aws_region)

@app.route("/", methods=["GET", "POST"])
def index():
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
            return f"Transcription started for {filename}. Check AWS Transcribe."
        except Exception as e:
            return f"Error starting transcription: {str(e)}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
