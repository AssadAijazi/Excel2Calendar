.PHONY: clean

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info 
	find . -name '*__pycache__' | xargs rm -fr 
	find . -name '*.pyc' | xargs rm -fr 

