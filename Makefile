PHONY: \
	__build-ci-image \
	clean \
	format-code \
	lint \
	send-coverage-report \
	test \
	update-requirements

DOCKER_RUN_ARGS = -v $(shell pwd):/code -u $$(stat -c "%u:%g" $(shell pwd))
CI_DOCKER_IMAGE_NAME = data-structure-ci
DOCKER_RUN = @docker run $(DOCKER_RUN_ARGS) $(CI_DOCKER_IMAGE_NAME)

__build-ci-image:
	@docker build -q -f .docker/ci.Dockerfile -t $(CI_DOCKER_IMAGE_NAME) .

clean:
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .cache
	@rm -rf .coverage
	@rm -rf coverage.xml
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.pyc' -delete

format-code: __build-ci-image
	$(DOCKER_RUN) isort -rc .
	$(DOCKER_RUN) black .

lint: __build-ci-image
	$(DOCKER_RUN) isort -rc -c .
	$(DOCKER_RUN) black --check .
	$(DOCKER_RUN) flake8
	$(DOCKER_RUN) mypy src

send-coverage-report: __build-ci-image
	@docker run \
		$(DOCKER_RUN_ARGS) \
		-e CODECOV_TOKEN="$$CODECOV_TOKEN" \
		$(CI_DOCKER_IMAGE_NAME) \
		codecov

test: __build-ci-image
	$(DOCKER_RUN) scripts/run_tests.sh

update-requirements: __build-ci-image
	$(DOCKER_RUN) scripts/update_requirements.sh
