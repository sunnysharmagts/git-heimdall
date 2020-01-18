vsecretfy: FORCE
	python3 -m venv ~/.vsecretfy/secretfy-config-creator
	echo . ~/.vsecretfy/secretfy-config-creator/bin/activate > vsecretfy

deps: FORCE
	. ./vsecretfy && pip3 install -r requirements-dev.txt

lint:
	#. ./venv && isort --quiet --diff --skip-glob "*/build/*"
	. ./vsecretfy/bin/activate && pylama secretfy_template


FORCE:
