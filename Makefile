.PHONY: clean

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info 
	find . -name '*.pyc' | xargs rm -fr 

