PHONY: \
	__build_test_image \
	clean \
	format-code \
	lint \
	test

__build_test_image:
	docker build -f .docker/test.Dockerfile -t data-structure-test .

clean:
	rm -rf .pytest_cache
	rm -rf tests/datastructures/__pycache__

format-code: __build_test_image
	docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		isort -rc .
	docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		black .

lint: __build_test_image
	docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		isort -rc -c .
	docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		black --check .
	docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		flake8

test: __build_test_image
	docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		./run_tests.sh
