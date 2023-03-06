
# Product Repository API

 Product Repository API based Django REST Framework

## Start

Create environment and install requirement using [poetry](https://python-poetry.org/)

```bash
# From directory with pyproject.toml file
$ poetry update
$ poetry shell
```

Or you can use old fashion pip with requirements.txt file

```bash
python3 -m venv tutorial-env
# On Windows, run:
tutorial-env\Scripts\activate.bat
# On Unix or MacOS, run:
source tutorial-env/bin/activate
# After activete venv installation requirements
pip install -r requirements.txt

```

The project use celery with RabbitMQ as broker. Previously start server need install [RabbitMQ](https://www.rabbitmq.com/download.html) and run it.

in .env file you can change environments from dev to prod use  DJANGO_ENV variable
After run the server use command:

```bash
python3 manage.py runserver
```

### API endpoints

```bash
http://127.0.0.1:8000/products/
#  GET request for get list of created products. Implemented bool parameter modified for get list of modified products or not.
# Example of response:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "uuid": "7122ddf8-5634-4503-8f87-c879b05643e5",
            "name": "name",
            "description": "description",
            "logo": "http://127.0.0.1:8000/static/logos/logo.jpg"
        },
    ]
}
#  POST request for create new product with body
# Example of body 
{
    "name": "name",
    "description": "description",
    "logo": "logo_path.pictures"
}


http://127.0.0.1:8000/products/{uuid}
# GET request for get product with uuid or DELETE for remove it or [PUT, PATCH] for update

```

## Credits

This software uses the following open source packages:

- Python = "^3.11"
- Django = "^4.1.7"
- django-filter = "^22.1"
- django-celery-results = "^2.4.0"
