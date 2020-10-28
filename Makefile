build:
	poetry build


publish:
	poetry publish --build


outdated:export http_proxy=http://127.0.0.1:8081
outdated:export https_proxy=http://127.0.0.1:8081
outdated:
	poetry show -o


update:export http_proxy=http://127.0.0.1:8081
update:export https_proxy=http://127.0.0.1:8081
update:
	poetry update
	make freeze

freeze:
	poetry export --without-hashes -f requirements.txt -o requirements.txt
