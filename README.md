# Flask-App

[![Build Status](https://travis-ci.org/karthikrk1/flask-app.svg?branch=master)](https://travis-ci.org/karthikrk1/flask-app)

## Introduction

Flask-App is an example microblog that is created using Python 3 (3.6 to be precise) and Flask and holds support for a majority of functions
that is supported in social media applications like Twitter. This app was built from scratch following the guide
developed by [Miguel Grinberg](https://blog.miguelgrinberg.com/).

## Features

The features of v1.0 of this app include the following:

* Creating Profile Pages
* Follower
* I18N and L10N
* Full Text Search
* Translation (If the posts are not in the original language of the user)

## Running this application on a local environment

### Prerequisites:

In order to run the app the following prerequisites are needed to be installed.

Python 2.7.x or Python 3.6.x
Elasticsearch - [Installation Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html)

#### Start Elasticsearch:

```
cd <elasticsearch-root-folder>
./bin/elasticsearch
```

#### Steps to run after these are set up: (Assuming a Linux or Mac terminal. Windows should also match closely)

1. Clone the repository

```
git clone https://github.com/karthikrk1/flask-app.git
```

2. Change to the project directory

```
cd flask-app
```

3. Create a python virtual environment

```
python -m venv <virtual-env-name>
```

This command creates a python virtual environment under the flask-app folder.

4. Activate the virtual environment

```
source <virtual-env-name>/bin/activate
```
This step is mandatory if you wish to keep your root installation of Python from being clean. The packages that will be
installed as part of the next step will only exist within the virtual environment and not in Python installation's root
folder

5. Install the requirements

```
pip install -r requirements.txt
```

7. Set some environment variables

```
export FLASK_APP=flask_app.py
```

Debug mode. -- This is needed only when running in a test environment; should be set to 0 in a PROD server

```
export FLASK_DEBUG=1
```

Email support. Uses Google's Email server. Can use other services if preferred

```
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-username>
export MAIL_PASSWORD=<your-gmail-password>
```

8. Running the app

```
flask run
```

This starts the application and can be viewed from the following URL: http://localhost:5000 in your laptop. Port can
be configured as needed.

#### Other useful shell commands:

##### DB Migrations

Initializing for the first time

```
flask db init
```

Migrations

```
flask db migrate -m "<your-message>"
```

Upgrade

```
flask db upgrade
```

Flask shell context

```
flask shell
```

This shell context contains all the necessary components initialized and does not need to be invoked. This can serve as
as a good place for running tests and for people who prefer a shell.

