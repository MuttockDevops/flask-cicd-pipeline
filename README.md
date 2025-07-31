# flask-cicd-pipeline
Flask app with Docker and GitHub Actions pipeline

##  Tech Stack

- Python 3.11
- Flask
- Docker
- GitHub Actions (CI)
- Pytest (for testing)
- WSL2 / Ubuntu (local dev)

## Features

- Dockerized development environment
- GitHub Actions pipeline that installs dependencies and runs tests on push
- Basic automated unit test using Pytest
- Simple "Hello DevOps World!" app to prove end-to-end flow
- Uses `.env` and `python-dotenv` for environment variable management
- Simple `/` and `/secret` routes to test config and flow
- Clean project structure with `venv`, `.gitignore`, and modular code

## Endpoints

- `/` → returns "Hello, DevOps World!"
- /secret` → pulls and returns `SECRET_KEY` from `.env` (for testing purposes only)

## Getting Started

### Clone the repo
```bash
git clone git@github.com:MuttockDevops/flask-cicd-pipeline.git
cd flask-cicd-pipeline
