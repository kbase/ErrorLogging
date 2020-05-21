# Allow the file "test" to not exist
# Remember to use tabs not spaces
.PHONY:test

TESTS := tests/unittest_errorlogfunctions.py

test:
	@echo "Running tests for $(TESTS)"
	PYTHONPATH=.:source:test pytest --cov-report=xml --cov source --verbose $(TESTS)
