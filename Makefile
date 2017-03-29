install:
	python setup.py install
test:
	python setup.py test
	pep8 fastread
	pyflakes fastread

	pytest --cov=fastread
