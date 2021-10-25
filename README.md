# Mini example of Flask and Flask-RESTX

![Actions Workflow](https://github.com/po5i/flask-mini-rest/workflows/Flask/badge.svg)

This is a examle repository for [my article](https://dev.to/po5i/how-to-add-basic-unit-test-to-a-python-flask-app-using-pytest-1m7a).

## Setup

Create and activate the virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Run the server

```bash
FLASK_ENV=development flask run
```

Run the tests

```bash
python -m pytest
```

The server will be up on [http://localhost:5000](http://localhost:5000)
and the API landing page will be available on [http://127.0.0.1:5000/api/v1/](http://127.0.0.1:5000/api/v1/).

## Requirements

Python >= 3.6

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)
