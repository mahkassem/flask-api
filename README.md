# Flask API

## Description

This is a simple Flask API that allows you to create, read, update and delete users and their posts.

## Dependencies

- Python 3.11

## Installation

Create a virtual environment and install the dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
# Or
pip install -e .
```

## Run (WSGI)

```bash
python wsgi.py

# * Running on http://127.0.0.1:8000
```

## Run (Flask)

```bash
flask run

# * Running on http://127.0.0.1:5000
```
