publish:
	poetry publish --build


freeze:
	poetry export --without-hashes -f requirements.txt -o requirements.txt
