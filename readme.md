# Python, ZeroMQ, Mongo Example

This example provides basic CRUD operations using a python flask container communicating using ZeroMQ to a business logic server layer further connected to a MongoDB container.

Of interest:

- Use of `docker-compose` to build and run the application
- Use of a persistent storage volume
- Use of ZeroMQ to pass messages to the business logic layer
