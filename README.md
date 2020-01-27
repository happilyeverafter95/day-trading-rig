# Setup

## Contributing to the repo

Make sure `direnv` is installed.

- Run `pip install -r requirements.txt` to install necessary dependencies
- Copy `.envrc.example` to `.envrc` and populate the environment variables
- Run `direnv allow`
- Run `pre-commit install` in the repo to enable pre-commit hooks

## Docker Setup

Run these commands to run the Docker Container. The web server will be available at `localhost:8080`.

`docker build . -t airflow`

`docker run -d -p 8080:8080 airflow webserver`
