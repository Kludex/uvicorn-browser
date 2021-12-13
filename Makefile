.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: lint
lint:  ## Linter the code.
	@echo "🚨 Linting code"
	isort uvicorn_browser tests --check
	flake8 uvicorn_browser tests
	mypy uvicorn_browser
	black uvicorn_browser tests --check --diff


.PHONY: format
format:
	@echo "🎨 Formatting code"
	isort uvicorn_browser tests
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place uvicorn_browser tests --exclude=__init__.py
	black uvicorn_browser tests


.PHONY: tests
test:  ## Test your code.
	@echo "🍜 Running pytest"
	pytest tests/ --cov=uvicorn_browser --cov-report=term-missing:skip-covered --cov-report=xml --cov-fail-under 100


.PHONY: publish
publish:  ## Publish release to PyPI
	@echo "🔖 Publish to PyPI"
	python setup.py bdist_wheel
	twine upload dist/*
