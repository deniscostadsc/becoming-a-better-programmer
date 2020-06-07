PHONY: \
	__build-ci-image \
	clean \
	format-code \
	lint \
	send-coverage-report \
	test \
	update-requirements

CI_DOCKER_IMAGE_NAME = data-structure-ci

__build-ci-image:
	@docker build -q -f .docker/ci.Dockerfile -t $(CI_DOCKER_IMAGE_NAME) .

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
		$(CI_DOCKER_IMAGE_NAME) \
		isort -rc .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		black .

lint: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		isort -rc -c .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		black --check .
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		flake8
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		mypy src

send-coverage-report: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		-e CODECOV_TOKEN="$$CODECOV_TOKEN" \
		$(CI_DOCKER_IMAGE_NAME) \
		codecov

test: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		scripts/run_tests.sh

update-requirements: __build-ci-image
	@docker run \
		-v $(shell pwd):/code \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		$(CI_DOCKER_IMAGE_NAME) \
		scripts/update_requirements.sh
