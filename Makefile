.PHONY: clean

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info 
	find . -name '*__pycache__' | xargs rm -fr 
	find . -name '*.pyc' | xargs rm -fr 
	pip uninstall XL2Cal -y

install:
	python setup.py sdist
	pip install dist/XL2Cal-1.0.dev0.tar.gz

clean-install: clean install
	