import psycopg2
import click


def connect_db():
	conn = psycopg2.connect(dbname="postgres",
				user="postgres",
				password="postgres")
	return conn
 
 
def drop_conn(conn):

	conn.commit()
	conn.close()


def init_db(conn):

	connection = conn()
	cur = connection.cursor()

	with open("schema.sql", "r") as file:
		cur.execute(file.read())

	drop_conn(connection)


def send_author_to_db(first_name: str, last_name: str):

	conn = connect_db()
	cur = conn.cursor()

	cur.execute(f"insert into authors (name, lastname) values ('{first_name}', '{last_name}');")

	drop_conn(conn)


def get_authors_from_db():

	conn = connect_db()
	cur = conn.cursor()

	cur.execute("select * from authors;")

	authors = cur.fetchall()

	return authors
	drop_conn(conn)


def delete_author_from_db(identifier: str, **kw):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"delete from authors where id = {identifier}")

    drop_conn(conn)


def send_book_to_db(title: str, author_id: int):

	conn  = connect_db()
	cur = conn.cursor()

	cur.execute(f"insert into books (title, author_id) values ('{title}', '{author_id}');")

	drop_conn(conn)


def get_books_from_db(*args, **kwargs):
	conn = connect_db()
	cur = conn.cursor()

	cur.execute("select * from books;")
	names = cur.fetchall()

	return names
	drop_conn(conn)


def update_book(identifier: str, **kw):

	conn = connect_db()
	cur = conn.cursor()

	cur.execute(f"update books set (title, author_id) = {kw['title'], kw['author_id']} where id = {identifier}")

	drop_conn(conn)


def delete_book(identifier: int, *args, **kwargs):

	conn = connect_db()
	cur = conn.cursor()

	cur.execute(f"delete from books where id = {identifier}")

	drop_conn(conn)


@click.command("init_db")
def init_db_command():
	init_db(connect_db)


def init_app(app):
	app.cli.add_command(init_db_command)

