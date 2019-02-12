FROM python:latest

WORKDIR /app

# Copy the python app and the web page templates into the container

COPY webapp.py .
COPY templates/* templates/

# Install the dependencies

RUN pip install pyzmq\
                flask\
                bson

# Run the web application

ENTRYPOINT ["python"]

CMD ["webapp.py"]