vheimdall: FORCE
	python3 -m venv ~/.vheimdall/git-heimdall
	echo . ~/.vheimdall/git-heimdall/bin/activate > vheimdall

deps: FORCE
	. ./vheimdall && pip3 install -r requirements-dev.txt

lint:
	#. ./venv && isort --quiet --diff --skip-glob "*/build/*"
	. ./vheimdall/bin/activate && pylama heimdall

FORCE:
