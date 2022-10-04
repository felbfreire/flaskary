import os

from flaskary import db

import pytest


os.environ["FLASK_APP"] = "flaskary"
os.system("flask init_db")

class TestDb:


    def test_insert_authorr(self):

        name = "Fred"
        last_name = "Nit"
        db.send_author_to_db(name, last_name)

        authors =  db.get_authors_from_db()

        assert authors[1] == (2, "Fred", "Nit")


    def test_delete_author_from_db(self):

        identifier = 2

        db.delete_author_from_db(identifier)

        authors = db.get_authors_from_db()

        assert authors == [(1, "John", "Tolkien")]


    def test_if_database_books_table_is_empty(self):

        books = db.get_books_from_db()

        assert books == []


    def test_get_from_db(self):

        title = "Lord of the rings - The two towers"
        author_id = 1
        db.send_book_to_db(title, author_id)

        books = db.get_books_from_db()

        assert books == [(1, "Lord of the rings - The two towers", 1)] 


    def test_update_book(self):

        identifier = 1
        title = "narn i chin hurin"
        author_id = "1" 

        db.update_book(
                identifier,
                title=title,
                author_id=author_id
        )

        books = db.get_books_from_db()

        assert books == [(1, "narn i chin hurin", 1)]


    def test_delete_id(self):
        
        identifier = 1

        db.delete_book(identifier)


