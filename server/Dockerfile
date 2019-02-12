FROM python:latest

WORKDIR /app

# Copy the application code to the app directory

COPY server.py .

# Install python packages required

RUN pip install pymongo\
                pyzmq

# Run the python server app

ENTRYPOINT ["python"]

CMD ["server.py"]