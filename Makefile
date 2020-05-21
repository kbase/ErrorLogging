# Allow the file "test" to not exist
# Remember to use tabs not spaces

.PHONY:test

test:
	python -m pytest tests/*
