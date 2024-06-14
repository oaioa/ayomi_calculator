# ayomi_calculator

## Tech

A Reverse Polish notation calculator in Python.

It uses **fastAPI** as web framework, and the requests are first handled by the ASGI server **uvicorn**.


**MondoDB** is used for storage.

## Docker compose

There are 2 containers, one for the mongodb instance and one for the web app.

```bash
docker-compose up --build
```
