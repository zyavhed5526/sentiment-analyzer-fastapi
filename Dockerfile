FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir fastapi uvicorn textblob pytest && python -m textblob.download_corpora

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
