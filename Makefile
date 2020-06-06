PHONY: \
	__build-test-image \
	clean \
	format-code \
	lint \
	send-coverage-report \
	test \
	update-requirements

__build-test-image:
	@docker build -q -f .docker/test.Dockerfile -t data-structure-test .

clean:
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .cache
	@rm -rf .coverage
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.pyc' -delete

format-code: __build-test-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		isort -rc .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		black .

lint: __build-test-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		isort -rc -c .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		black --check .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		flake8
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		mypy src

send-coverage-report: __build-test-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		-e CODECOV_TOKEN="$$CODECOV_TOKEN" \
		data-structure-test \
		codecov

test: __build-test-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		scripts/run_tests.sh

update-requirements: __build-test-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-test \
		scripts/update_requirements.sh
