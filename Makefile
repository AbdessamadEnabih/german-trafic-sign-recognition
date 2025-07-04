.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[.a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: init
init: install-deps download-data  ## Initialize the project environment and install dependencies.
	@echo "Project environment initialized and dependencies installed successfully."

.PHONY: init-venv 
init-venv: ## Initialize a virtual environment and install dependencies.
	python -m venv .venv
	@make install-deps
	@echo "Virtual environment initialized and dependencies installed successfully."
	@make download-data

.PHONY: install-deps 
install-deps: ## Install project dependencies.
	@.venv/Scripts/pip install -r requirements.txt || .venv/bin/pip install -r requirements.txt || pip install -r requirements.txt

.PHONY: download-data 
download-data: ## Download the dataset.
	@.venv/Scripts/python src/prepare_data.py || .venv/bin/python src/prepare_data.py || python src/prepare_data.py
	@echo "Dataset downloaded successfully."

