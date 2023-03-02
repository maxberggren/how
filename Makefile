PACKAGE_NAME = how
VERSION = 0.1.0

.PHONY: clean build install

clean:
	rm -rf dist/
	rm -rf $(PACKAGE_NAME).egg-info/

build:
	python3 setup.py sdist bdist_wheel

install: clean build
	pip3 uninstall -y $(PACKAGE_NAME)
	pip3 install dist/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl
	make clean