env:
	python3 -m venv venv
	./venv/bin/pip install -U pip
	./venv/bin/pip install -r pre_requirements.txt

run:
	MLFLOW_CONDA_HOME=~/anaconda3 ./venv/bin/mlflow run .
