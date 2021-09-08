# Raptor

Raptor is a high performance Discord moderation bot.

## Setup

Clone the repository and navigate to its directory in your terminal of choice.

Run `poetry install` to install the bot's dependencies.

Copy `.env.example` to `.env` and fill out the values.

Run `poetry run task watch-api` to start the API in watch/development mode.

Run `poetry run task start-api` to start the API in production mode.

Run `poetry run task start-bot` to start the API in production mode.

Note: there is no 'watch' mode for the bot.

When running in production it is recommended to use the included docker compose setup.
