.PHONY: venv install data process notebook report clean advanced-analysis

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

data:
	$(PYTHON) scripts/download_data.py

process:
	$(PYTHON) scripts/process_data.py

notebook:
	$(VENV)/bin/jupyter lab

report:
	$(VENV)/bin/jupyter nbconvert --to html --execute notebooks/analysis_eu_us.ipynb --output-dir reports

advanced-analysis:
	$(PYTHON) scripts/advanced_analysis.py

clean:
	rm -rf data/raw/* data/processed/* reports/*

