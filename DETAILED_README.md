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

## Languages Supported

The Flask-App can work in the following languages as of v1.0:

* English (Default)
* Tamil
* Spanish (Thanks to Miguel's Repo for Spanish translations)

## Support for international Dates and Times

Since time is not a common theme across different parts of the world, the server is set to take updates in UTC
(Coordinated Universal Time) and [momentjs](https://momentjs.com/) is used to convert this into different timezones
based on the browser's
current configuration.

## Support for Internationalization and Localization (I18N and L10N):

In order to provide the support for users from different language background the app is designed in English as the
primary language of choice while also supporting two other languages - Tamil and Spanish. There is also a Translate
service that uses Microsoft's Translator API (available in the Azure store) to translate some posts that are not
shown in the user's home language. This is done as an AJAX call.

## Profile Pages, Followers and Contacts:

This app is intended to be a clone of popular social media websites like Twitter and Facebook, so there is support for
creation and update of Profile Pages with support for Avatars through the support of gravatar. This means, there is also
support for finding other people and connecting to them through 'follow' requests. There is also support for Posts which
can be uploaded to the user's page and can be found in the index page of the user.

## Full Text Search

Searching for a post is also possible through the use of [Elasticsearch](https://www.elastic.co/).

Elasticsearch is a open source search engine based out of Lucene and supports indexing of documents and querying from
the index. The posts made by the user is always indexed through DB events which keep the indexes updated with a User's
latest post and thus search is performed on newly created posts with ease.


## Flask's Jinja2 template Engines

Flask has the support of Jinja2 a template Engine which helps to render the HTML pages with ease. This app leverages
this awesome feature of Flask to create a good experience for the users.

## Flask's extensions

Flask supports various extensions to create great apps. The various Flask extensions used:

* flask-sqlalchemy : An ORM for Flask which can be used to connect to various DB engines
* flask-moment: A Flask based Python wrapper for momentjs support.
* flask-babel: A Flask based extension of pybabel that is used for I18N and L10N
* flask-migrate: A Flask based version of Alembic to support migrations to DB
* flask-login: A Flask extension to support User logins
* flask-mail: A Flask extension to support Email services
* flask-Bootstrap: A Flask based wrapper for bootstrap to create awesome UI
* flask-WTF: A Flask extension for creating web forms
