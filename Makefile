.PHONY: default init bdd test format sort lint

default: test format sort lint

bdd: mamba format sort lint

init:
	poetry install

serve:
	bash ./scripts/serve.sh

test:
	bash ./scripts/pytest.sh

format:
	bash ./scripts/format.sh

lint:
	bash ./scripts/lint.sh

sort:
	bash ./scripts/sort.sh

mamba:
	bash ./scripts/mamba.sh

api:
	bash ./scripts/serve_api.sh