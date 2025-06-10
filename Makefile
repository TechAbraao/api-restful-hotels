.PHONY: help flask-run create-database

FLASK_APP=src.app.app
VENV=.venv/bin/flask
PYTHON=python3

help:
	@echo " * Available commands:"
	@echo "   flask-run       - Starts the Flask application"
	@echo "   create-database - Create the database"

flask-run:
	@echo " * Running Flask application..."
	@FLASK_APP=$(FLASK_APP) $(VENV) run

create-database:
	@echo " * Creating Database..."
	@$(PYTHON) src/app/scripts/create_db.py
