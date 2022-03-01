.DEFAULT_GOAL := help


.PHONY: help
help: ## Generates a help README
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


IMAGE ?= todo
.PHONY: build-api
build-api: ## Builds this project into a docker image
	@cd todo_api/ && docker build -f Dockerfile.api . -t "$(IMAGE)_api"


.PHONY: test-api
test-api: build ## Run backend tests
	@docker-compose run api sh test.sh


.PHONY: lint-api
lint-api: build ## Lint backend
	@docker-compose run api sh lint.sh


.PHONY: build-client
build-client: ## Builds this project into a docker image
	@cd todo_client/ && docker build -f Dockerfile.client . -t "$(IMAGE)_client"


.PHONY: lint-client
lint-client: build-client ## Lint frontend
	@docker-compose run client yarn lint


.PHONY: test-client
test-client: build-client ## Run frontend tests
	@docker-compose run client yarn test


.PHONY: start
start: ## Starts the Docker containers
	@docker-compose up


.PHONY: start-init
start-init: ## Re-build and Start the Docker containers
	@docker-compose up --build


.PHONY: stop
stop: ## Stops the Docker containers
	@docker-compose down


.PHONY: migration
migration: ## Create migrations using alembic
	@docker-compose run api alembic revision --autogenerate -m "@"


.PHONY: migrate-up
migrate-up: ## Runs the database migration
	@docker-compose run api alembic upgrade head


.PHONY: migrate-down
migrate-down: ## Rollback migrations using alembic
	@docker-compose run api alembic downgrade -1
