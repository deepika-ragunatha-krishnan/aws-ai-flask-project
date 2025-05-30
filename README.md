# AWS AI Flask Applications – NLP & Speech Demos

This repository includes **four lightweight Flask apps** showcasing Amazon AI services — **Comprehend** for NLP and **Transcribe** for speech-to-text.

Each app has a minimal interface and demonstrates a key AWS ML capability.

---

## 📁 Project Structure

```
aws-ai-flask-projects/
├── aws-ai-flask-comprehend/
│   ├── main.py
│   └── templates/index.html

├── aws-ai-flask-sentiment-analysis/
│   ├── main.py
│   └── templates/index.html

├── aws-ai-flask-transcribe-on-screen/
│   ├── main.py
│   └── templates/index.html

├── aws-ai-flask-transcription/
│   ├── main.py
│   └── templates/index.html
```

---

## 🔹 1. Amazon Comprehend – Entity Detection

**Folder**: `aws-ai-flask-comprehend`  
**Purpose**: Detect entities such as persons, organizations, dates, and places in user input.

### 🧪 Example Input

```text
Jeff Bezos founded Amazon in Seattle in 1994.
```

### ✅ Sample Output

```text
Entity: Jeff Bezos (PERSON)
Entity: Amazon (ORGANIZATION)
Entity: Seattle (LOCATION)
Entity: 1994 (DATE)
```

---

## 🔹 2. Amazon Comprehend – Sentiment Analysis

**Folder**: `aws-ai-flask-sentiment-analysis`  
**Purpose**: Analyze the sentiment of a sentence (Positive, Negative, Neutral, or Mixed)

### 🧪 Example Input

```text
I love using AWS tools for AI applications.
```

### ✅ Sample Output

```text
Sentiment: POSITIVE
Confidence: 95.2%
```

---

## 🔹 3. Amazon Transcribe – Live Transcription to Screen

**Folder**: `aws-ai-flask-transcribe-on-screen`  
**Purpose**: Capture microphone input and transcribe it live to screen using streaming.

### 💡 Features

- Real-time transcription with low latency  
- Simple UI displaying live speech-to-text

---

## 🔹 4. Amazon Transcribe – Audio File Upload & Transcription

**Folder**: `aws-ai-flask-transcription`  
**Purpose**: Upload an audio file (MP3/WAV) and receive a transcription from Amazon Transcribe.

### 🧪 Workflow

1. Upload audio file  
2. Start AWS Transcribe job  
3. Fetch and display transcript

---

## 🚀 How to Run Any Flask App

```bash
# Step 1: Navigate to any project folder
cd aws-ai-flask-comprehend  # or any of the others

# Step 2: (Optional) Setup virtual environment
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# Step 3: Install required packages
pip install flask boto3

# Step 4: Run the Flask app
python main.py
```

---

## 🔐 AWS Configuration

Ensure your AWS CLI is configured with appropriate permissions:

```bash
aws configure
```

### Required IAM Permissions

```text
comprehend:DetectEntities  
comprehend:DetectSentiment  
transcribe:StartTranscriptionJob  
transcribe:GetTranscriptionJob
```

---

## ⚙️ Tech Stack

| Component       | Technology                    |
|----------------|-------------------------------|
| Backend         | Python 3.x                    |
| Framework       | Flask                         |
| Cloud Services  | Amazon Comprehend, Transcribe |
| Frontend        | HTML (Jinja2 templates)       |

---

## 📄 License

This project is intended for **educational and demonstration purposes only**.

---

## 👩‍💻 Author

**Deepika Ragunatha Krishnan**  
Capstone Projects – Humber College, 2025  
AWS Cloud + AI Integration Demos
