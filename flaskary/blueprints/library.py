from flask import Blueprint, request, jsonify

from .db import send_author_to_db, get_authors_from_db, send_book_to_db, get_books_from_db, update_book, delete_book
				


bp = Blueprint("library", __name__)


@bp.route("/", methods=["GET"])
def main_page():

	return "<p>/send</p><p>/get</p><p>/update_id</p><p>/delete_id</p>"


@bp.route("/send_author", methods=["POST"])
def send_author():
	
	first_name = request.json["first_name"]
	last_name = request.json["last_name"]

	send_author_to_db(first_name, last_name)

	return jsonify("Sucess")


bp.route("/get_authors", methods=["GET"])
def get_authors():

	return get_authors_from_db()


@bp.route("/send", methods=["POST"])
def send_book():

	title = request.json["title"]
	author_id = request.json["author_id"]

	if title and author_id:
		send_book_to_db(title, author_id)

		return jsonify("Success")


@bp.route("/get", methods=["GET"])
def get():

	return get_books_from_db()


@bp.route("/update/<identifier>/<new_title>/<new_author_id>", methods=["POST"])
def update(identifier, new_title, new_author_id):

	update_book(identifier, title=new_title, author_id=new_author_id)
	return b"<p>id {identifier} was been updated</p>"


@bp.route("/delete/<identifier>", methods=["GET"])
def delete(identifier):

	delete_book(identifier)
	return b"<p>id {identifier} was been deleted</p>"
