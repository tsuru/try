clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

test-deps:
	@pip install -r test-requirements.txt

test: test-deps
	@py.test -s .
	@flake8 .

run:
	@honcho start
