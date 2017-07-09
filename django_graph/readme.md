# Django Graph

- A Django app that exposes a RESTful API endpoint for a random number generator and display a graph using a streaming plot.ly graph.

# Setup

- Create a python virtual environment:
  - Ensure you have `pip` installed
  - Install `python virtual enviroment` on your machine: `pip install virtualenv`
  - `cd` into the directory where the project has been cloned, then `cd` into `django_graph` directory
  - Create a `virtual env` within the `django_cache` directory:  `virtualenv .env`
  - Activate the virtual environment: `source .env/bin/activate`
  - Install project dependencies within the activated virtual environment: `pip install -r requirements.txt`
  - Run django migrations: `python manage.py migrate`

N/B - ensure you have redis-server installed on your machine

# Project Structure

- The project is has two main `apps`:
  - `api` -  this contains the `random generator` api, and consumers for all the websockets communications
  - `ui` - this contains the 'frontend' side of the app, showing a page where the graph is plotted

  Other directories:
    - `static_files/js` - this contains the `plot.js` file that manages creating websocket connection,
    listening to the created connection, and plotting the graph
    - `config` - this contains the application's settings file


# Testing

- Graphing page:
  - The page is accessible at:  `http://localhost:8000/plot/`

- Random Generator endpoint:
  - The endpoint is available at: `http://localhost:8000/api/v1/random/`
  - Then you do a `POST` to this endpoint, a random number is generated, and
  the graph is automatically updated

