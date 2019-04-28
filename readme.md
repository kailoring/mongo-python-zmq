
# Python, ZeroMQ, Mongo

Simple Ansible application with CRUD functionality that uses a python flask container with ZeroMQ to work with a business logic server layer while being connected to a MongoDB container. The application uses a persistent storage volume.

Once the playbook is ran, application is found on localhost:8001

## Files

- `ExamplePlaybook.yaml`

Responsible for building the webclient, server and database containers. In this file you also create the appropriate volumes and define the services you wish to start.

## Directories

### mongo

This directory contains the files necessary to initiate the database. It further inserts a couple of records into the database.

### server

This directory contains the files necessary to build the web server using a python app.

### webclient

This directory contains the code to run the python application using the flask package.
