# Flask

## Setting Up Locally

- Check that Python 3 is installed (newer than 3.4)
  ```
  $ python3 --version   # Python 3.7.3
  ```
- Create a virtual environment
  ```
  $ python3 -m venv flaskenv
  ```
- Activate the environment
  ```
  $ source venv/bin/activate
  ```
- Install Flask
  ```
  $ pip install flask
  ```
- Set `FLASK_APP` environment variable so that Flask knows how to import and run the app
  ```
  $ export FLASK_APP=index.py
  ```
- Run the app
  ```
  $ flask run
  ```
## Setting Up in Docker

-
