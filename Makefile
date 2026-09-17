PY = .venv/bin/python3
#what if it is already exits?
VENV = .venv
#VENV_BIN = $(VENV)/bin
CFG = config.txt
MAIN = a-maze-ing.py
OTP = maze.txt
MYPY_F = --explicit-package-bases --warn-return-any \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

# can be ommited?
all: run

install:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install mlx-2.2-py3-none-any.whl
	$(PY) -m pip install -r requirements.txt
	
run: install
	$(PY) $(MAIN) 

build:
	$(PY) -m build  
#	cp dist/mazegen-1.0.0-py3-none-any.whl .

lint:
	flake8
	mypy . $(MYPY_F)

debug:
	$(PY) -m pdb $(MAIN) $(CONFIG)

clean:
	rm -rf .venv .mypy_cache .pytest_cache build dist *.egg-info $(OTP)
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: install run build lint debug clean