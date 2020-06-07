PHONY: \
	__build-ci-image \
	clean \
	format-code \
	lint \
	send-coverage-report \
	test \
	update-requirements

__build-ci-image:
	@docker build -q -f .docker/ci.Dockerfile -t data-structure-ci .

clean:
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .cache
	@rm -rf .coverage
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.pyc' -delete

format-code: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		isort -rc .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		black .

lint: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		isort -rc -c .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		black --check .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		flake8
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		mypy src

send-coverage-report: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		-e CODECOV_TOKEN="$$CODECOV_TOKEN" \
		data-structure-ci \
		codecov

test: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		scripts/run_tests.sh

update-requirements: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		data-structure-ci \
		scripts/update_requirements.sh
