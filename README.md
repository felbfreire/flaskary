Flaskary is a project that uses The minimalist web framework Flask, postgresql database and requests. Also
used pytest for testing. Ill add coverages someday in the future ..

Author: Felipe Freire - felbfreire 
repo: https://github.com/felbfreire/flaskary.git


-- Installing dependencies --

-> create a virtual enviroment for installing all its dependencies:

$ python -m venv venv

-> upgrade pip:

$ pip install --upgrade pip:

-> and install using requirements.txt:

$ pip install -r requirements.txt

-- initializing database --

 assuming that postgres is installed and configured and postgres user has password 'postgres':

$ source init.sh


$ flask init_db

-- Using the flaskary with Requests python package --
 
 $ flask run


 if it runs well, you are now serving on localhost 127.0.0.1:5000.
 open another terminal, source that venv again, and enter python interactive prompt:

$ source venv

$ python


>>> import requests

 lets insert some book in table:

>>> requests.post("http://127.0.0.1:5000/send", json={"title": "Unfinished tales", "author_id": 1})

 we can fetch all information from the books table:

>>> requests.get("http://127.0.0.1:5000/get").json()

[[1, "Unfinished tales", 1]]

 We can also updated it using the post method:

>>> requests.post("htpp://127.0.0.1:5000/update/1/The Silmarilion/1")

 If you want to check if the table was updated, just fetch it again:

>>> requests.get("http://127.0.0.1:5000/get").json()

