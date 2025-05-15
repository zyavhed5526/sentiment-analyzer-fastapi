# Sentiment Analyzer FastAPI

This project is a simple REST API built using FastAPI that performs sentiment analysis on input text using TextBlob.  

## Features

- Health check endpoint (`GET /`)  
- Sentiment analysis endpoint (`POST /analyze`) that returns sentiment (positive/negative/neutral) and polarity score  

## Project Structure

- `main.py`: The FastAPI application code  
- `test_main.py`: Automated tests for the API endpoints using pytest  
- `requirements.txt`: Python dependencies  
- `Dockerfile`: To build the application image in Docker  
- `venv/`: Virtual environment folder (ignored in GitHub)  

## Prerequisites

- Python 3.10+ installed  
- Git installed  
- (Optional) Docker installed for containerized deployment  

## Setup and Running Locally

1. **Clone the repository**


git clone https://github.com/zyavhed5526/sentiment-analyzer-fastapi.git

cd sentiment-analyzer-fastapi

2. **Create a virtual environment**
python3 -m venv venv

3. **Activate the virtual environment**
source venv/bin/activate

4. **Install dependencies**
pip install -r requirements.txt

5. **Run the FastAPI app**
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000/

6. **Test the API**
Open a browser and visit http://127.0.0.1:8000/docs to access the automatic interactive API docs (Swagger UI).

Try the /analyze POST endpoint by entering text and see sentiment analysis in action.

7. **Running with Docker (optional)**

Make sure Docker is installed and running.

Build Docker image


docker build -t sentiment-api .
Run Docker container


docker run -p 8000:8000 sentiment-api
Access the API

Go to http://localhost:8000/docs in your browser.