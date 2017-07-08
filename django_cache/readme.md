# Django API Caching Middleware

- Middleware to cache specific defined APIs.

# Setup

- Create a python virtual environment:
  - Ensure you have `pip` installed
  - Install `python virtual enviroment` on your machine: `pip install virtualenv`
  - `cd` into the directory where the project has been cloned, then `cd` into `django_cache` directory
  - Create a `virtual env` within the `django_cache` directory:  `virtualenv .env`
  - Activate the virtual environment: `source .env/bin/activate`
  - Install project dependencies within the activated virtual environment: `pip install -r requirements.txt`
  - Run django migrations: `python manage.py migrate`

# Testing

- Three endpoints have been defined:
  -  GET - `/api/v1/cached` -  will always be cached
  -  POST - `/api/v1/cached` -  will never be cached
  -  GET - `/api/v1/not_cached` -  will never be cached

- Run `python manage.py test` to test the caching middleware, for the above endpoints
