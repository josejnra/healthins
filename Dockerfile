FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

COPY ./app /app

RUN pip install -r /app/requirements.txt

ENV ENV_FILE_PATH "/app/.env"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
