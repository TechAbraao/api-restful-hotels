.PHONY: help flask-run

help:
	@echo " > Available commands:"
	@echo "   flask-run   - Starts the Flask application"

flask-run:
	@echo " > Running Flask application..."
	@FLASK_APP=src.app.app .venv/bin/flask run
