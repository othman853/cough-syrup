.SILENT:
VENV_NAME := .venv

run-dev:
	export PYTHONPATH=. && $(VENV_NAME)/bin/python3 main.py
venv:
	sh bin/venv.sh . $(VENV_NAME)
install-dev:
	$(VENV_NAME)/bin/pip3 install -r requirements/development.txt
test-unit:
	$(VENV_NAME)/bin/pip3 install -r requirements/test.txt
	export PYTHONPATH=. && $(VENV_NAME)/bin/py.test tests/unit
test-functional:
	$(VENV_NAME)/bin/pip3 install -r requirements/test.txt
	export PYTHONPATH=. && $(VENV_NAME)/bin/py.test tests/functional
clean:
	sh bin/clean.sh . '__pycache__'
	sh bin/clean.sh tests '.cache'
