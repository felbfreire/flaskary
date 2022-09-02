import os

import requests
import pytest

os.environ["FLASK_APP"] = "flaskary"
os.system("flask init_db")

class TestCli:


	def test_if_send_request_returns_status_code_200_OK(*args, **kwargs):
		requests.post("http://127.0.0.1:5000/send", json={"title": "Tom Bombadil", "author_id": 1}).status_code == "200"


	def test_if_get_request_returns_status_code_200_OK(*args, **kwargs):
		requests.get("http://127.0.0.1:5000/get").status_code == "200"


	def test_if_update_request_returns_status_code_200_OK(*args, **kwargs):
		requests.post("http://127.0.0.1:5000/update/1/Unfinished tales/1").status_code == "200"


	def test_if_delete_request_returns_status_code_200_OK(*args, **kwargs):
		requests.get("http://127.0.0.1:5000/delete/1").status_code == "200"

