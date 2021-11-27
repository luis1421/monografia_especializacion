FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1 

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt .

COPY ./src .

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "nlp_app:app"]