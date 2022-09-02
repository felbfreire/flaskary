from flask import Flask

from .blueprints import	library ,db


def create_app():
	app = Flask(__name__)

	db.init_app(app)
	app.register_blueprint(library.bp)

	return app
