init:
	# pip install -r requirements.txt    # No requirements necessary
	chmod +x run.py

test:
	py.test tests

test_basic:
	cat tests/test_basic.txt | python3 tests/test_basic.py


.PHONY: init test test_basic
