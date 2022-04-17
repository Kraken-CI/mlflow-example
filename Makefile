env:
	python3 -m venv venv
	./venv/bin/pip install -U pip
	./venv/bin/pip install -r pre_requirements.txt

	wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
	chmod a+x Anaconda3-2021.11-Linux-x86_64.sh
	./Anaconda3-2021.11-Linux-x86_64.sh -b || true

run:
	MLFLOW_CONDA_HOME=~/anaconda3 ./venv/bin/mlflow run .
