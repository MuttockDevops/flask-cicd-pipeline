flask-cicd-pipeline
Flask web application powered by Docker and GitHub Actions, with a complete CI pipeline including automated testing and code coverage reporting.

Tech Stack
Python 3.11

Flask

Docker & Docker Compose

GitHub Actions (CI/CD)

Pytest & Pytest-Cov – for testing and code coverage

python-dotenv – for managing secrets via .env

Render – for deployment

WSL2 / Ubuntu – for local development

Features
Dockerized development and production-ready environment

GitHub Actions pipeline: builds Docker image, runs unit tests, checks test coverage

Test coverage results printed in CI output

Uses .env + python-dotenv to manage environment variables

Clean modular Flask app structure

CI Pipeline Includes:
Code checkout

Docker build

Pytest execution

Coverage reporting

Automatically deploys to Render on main branch pushes

Clean virtual environment setup, .gitignore, and organized project layout

Endpoints
Route	Description
/	Returns Hello, DevOps World!
/secret	Returns the SECRET_KEY from .env

Testing & Coverage
Unit tests live in the tests/ directory.

Run locally with:

docker compose run --rm web pytest --cov=app
Coverage results are also shown in GitHub Actions workflows under the “Run tests with coverage” step.

Deployment
Live at:
https://flask-cicd-pipeline.onrender.com

Pushes to main will trigger automatic redeploys on Render.

Getting Started Locally


Clone the repository:
git clone https://github.com/MuttockDevops/flask-cicd-pipeline.git
cd flask-cicd-pipeline

Create a .env file:
SECRET_KEY=your-super-secret-key

Build and run the application:
docker compose build
docker compose up

Then visit:
http://localhost:5000
