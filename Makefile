init:
	pip install -r requirements.txt

lint:
	#. ./venv && isort --quiet --diff --skip-glob "*/build/*"
	. ./vsecretfy/bin/activate && pylama secretfy_template
