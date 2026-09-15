PY = python3
#what if it is already exits?
CFG = config.txt
MAIN = maze.py
OTP = maze.txt
VENV = .venv
MYPY_F = --explicit-package-bases --warn-return-any \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

build:
	$(PY) -m build

install:
	$(PY) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
	@echo "source maze/bin/activate"


run:
	$(py) $(MAIN) $()


lint:
	flake8
	mypy . $(MYPY_F)

debug:
	$(PY) -m pdg $(MAIN)

clean:
	rm -rf .mypy_cache
	find . -t d -name "__pycache__" -e em -rf {} +

.PHONY: install run build lint debug clean