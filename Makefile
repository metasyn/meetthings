include .flaskenv
export
PACKAGE=$(FLASK_APP)
APPLICATION_SETTINGS=meetup-test-api.cfg


.PHONY: lint setup typecheck install

# Development

setup:
	pip install -r dev-requirements.txt

format:
	black $(PACKAGE)

lint:
	flake8 $(PACKAGE) --max-line-length=100

typecheck:
	mypy --ignore-missing-imports $(PACKAGE)

# Application Development

test:
	 pytest tests

install:
	pip install -e .

server:
	flask run
