FROM python:latest

COPY . /app
COPY templates/* /app/templates/

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]