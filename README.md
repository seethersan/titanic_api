# TITANIC API

This project is a Flask API for a model to predict if a passenger would survive or not

## Run with virtualenv

### Create virtualenv

```bash
virtualenv .env
source .env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run API

```bash
python api.py 6000
```

## Run with docker-compose

```bash
docker-compose up -d
```

By default the API maps port 6000

## Example Request

```json
[
  { "Age": 85, "Sex": "male", "Embarked": "S" },
  { "Age": 24, "Sex": "female", "Embarked": "C" },
  { "Age": 3, "Sex": "male", "Embarked": "C" },
  { "Age": 21, "Sex": "male", "Embarked": "S" }
]
```

The body needs to have this format
