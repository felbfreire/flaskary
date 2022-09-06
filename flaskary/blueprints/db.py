import psycopg2
import click


def cursor():

    conn = psycopg2.connect(dbname="postgres",
                user="postgres",
                password="postgres")

    cur = conn.cursor()

    return cur 
 
 
def drop_conn(cursor):
    
    cur = cursor

    cur.connection.commit()
    cur.connection.close()


def init_db():

    cur = cursor()

    with open("schema.sql", "r") as file:
        cur.execute(file.read())

    drop_conn(cur)


def send_author_to_db(first_name: str, last_name: str):

    cur = cursor()

    try:
        cur.execute(f"insert into authors (name, lastname) values ('{first_name}', '{last_name}');")
    except psycopg2.Error as e:
        print(e.diag.severity)

    drop_conn(cur)


def get_authors_from_db():

    cur = cursor()

    try:
        cur.execute("select * from authors;")
    except psycopg2.Error as e:
        print(e.diag.severety)

    authors = cur.fetchall()

    return authors
    drop_conn(cur)


def delete_author_from_db(identifier: str, **kw):

    cur = cursor()

    try:
        cur.execute(f"delete from authors where id = {identifier}")
    except psycopg.Error as e:
        print(e.diag.severity)

    drop_conn(cur)


def send_book_to_db(title: str, author_id: int):

    cur = cursor()

    try:
        cur.execute(f"insert into books (title, author_id) values ('{title}', '{author_id}');")
    except psycopg2.Error as e:
        print(e.diag.severity)

    drop_conn(cur)


def get_books_from_db(*args, **kwargs):

    cur = cursor()

    try:
        cur.execute("select * from books;")
    except psycopg2.Error as e:
        print(e.diag.severity)

    names = cur.fetchall()

    return names
    drop_conn(cur)


def update_book(identifier: str, **kw):

    cur = cursor()

    try:
        cur.execute(f"update books set (title, author_id) = {kw['title'], kw['author_id']} where id = {identifier}")
    except psycopg2.Error as e:
        print(e.diag.severity)

    drop_conn(cur)


def delete_book(identifier: int, *args, **kwargs):

    cur = cursor()

    try:
        cur.execute(f"delete from books where id = {identifier}")
    except psycopg2.Error as e:
        print(e.diag.severity)

    drop_conn(cur)


@click.command("init_db")
def init_db_command():
	init_db()


def init_app(app):
	app.cli.add_command(init_db_command)

