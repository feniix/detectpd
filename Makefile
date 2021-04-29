.PHONY: format
format:
	pipenv run autoflake --in-place --expand-star-imports --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables *.py
	pipenv run black *.py
	pipenv run isort --profile black .
