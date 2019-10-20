init:
	pip install -r requirements.txt

lint:
	#. ./venv && isort --quiet --diff --skip-glob "*/build/*"
	. ./venv && pylama
