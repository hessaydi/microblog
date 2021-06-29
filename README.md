# DJANGO REST API MICROBLOG

## TECHNOLOGIES USED
- **Python3.9**: [Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively

- **Django 3.1**: [Django](https://docs.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

- **Django REST framework**: [Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs

- **Django REST framework JWT**: [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework.

- **Celery - Distributed Task Queue**: [Celery](https://docs.celeryproject.org/en/stable/) is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.

- **Django Celery Beat - Database-backed Periodic Tasks**: [Django Celery Beat](https://django-celery-beat.readthedocs.io/) This extension enables you to store the periodic task schedule in the database

- **RabbitMQ - Messages Broker**: [RabbitMQ](https://www.rabbitmq.com/documentation.html/) it is software where queues are defined, to which applications connect in order to transfer a message or messages.


## SETTING UP THE PROJECT

### Clone the project
```
$ git clone https://github.com/hessaydi/microblog.git
$ cd django-rest-api-yummy-recipes
```

### Create the virtual environment and active it.
```
$ python -m venv env
$ source env/bin/activate
```

### Install the requirements
```
$ pip install -r requirements.txt
```

## RUN  UP THE DATABASE

### Migrate the migrations

```
$ python manage.py migrate
```

## Run the server
```
$ python manage.py runserver
```

## RUN THE APP ON BROWSER

    Execute the url **localhost:8000/api/** in your browser

    **password:** normaluser1234 for complete swagger-docs

### RUN TASKS USING CELERY AND RABBITMQ

```
$ brew install rabbitmq
$ celery -A core woker -l info
$ brew services start rabbitmq
```
### RUN SCHEDULE TASK MANAGER DJANGO CELERY BEAT
```
$ celery -A core beat -l info
```

## TODO: Functionality 
1. An authenticated user can add/delete a hashtag to/from their favorites.(not completed yet)


## API Documentation
Visit the links below for the API documentation

[Django Rest API Framework Documentation ](https://www.django-rest-framework.org/)
[Django Framework Documentation](https://docs.djangoproject.com/)
