# Electricity Bill Calculator

[![CI Pipeline](https://github.com/SRP500005/electricity-bill-calculator/actions/workflows/pipeline.yml/badge.svg)](https://github.com/SRP500005/electricity-bill-calculator/actions/workflows/pipeline.yml)

A simple Python command-line application that calculates an electricity bill from consumption in kilowatt-hours and price per kilowatt-hour.

This project demonstrates continuous integration and continuous delivery using pytest, GitHub Actions, Docker, and GitHub Container Registry.

## Features

- Calculate electricity costs from consumption and unit price.
- Reject negative consumption and negative prices.
- Handle non-numeric keyboard input.
- Display the bill with two decimal places.
- Run six automated tests.
- Build and check a Docker image automatically.
- Publish Docker images when changes are pushed to main.

## Calculation

Total bill = Consumption in kWh × Price per kWh

Example:

```text
Enter electricity consumption in kWh: 150
Enter price per kWh in euros: 0.30
Your electricity bill is €45.00
```

The calculator estimates consumption costs only. It does not include standing charges, additional taxes, or tiered tariffs.

## Technologies

- Python
- pytest
- Git
- GitHub Actions
- Docker
- GitHub Container Registry (GHCR)

## Project Structure

```text
electricity-bill-calculator/
├── app.py
├── requirements-dev.txt
├── tests/
│   └── test_app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .github/
│   └── workflows/
│       └── pipeline.yml
└── README.md
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/SRP500005/electricity-bill-calculator.git
cd electricity-bill-calculator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows using Git Bash:

```bash
source .venv/Scripts/activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

Run the calculator:

```bash
python app.py
```

The application uses Python's standard library and requires no additional runtime packages.

## Run Automated Tests

Install the test dependency:

```bash
python -m pip install -r requirements-dev.txt
```

Run the tests:

```bash
python -m pytest -v
```

The six tests cover:

1. Normal bill calculation.
2. Zero electricity consumption.
3. Zero price per unit.
4. Rounding to two decimal places.
5. Rejection of negative consumption.
6. Rejection of negative prices.

## Build and Run with Docker

Docker must be installed and running.

Build the image:

```bash
docker build -t electricity-bill-calculator:local .
```

Run the calculator interactively:

```bash
docker run --rm -it electricity-bill-calculator:local
```

If Windows Git Bash reports a TTY error, use:

```bash
winpty docker run --rm -it electricity-bill-calculator:local
```

## Run the Published Image

After a successful publish job, download the image:

```bash
docker pull ghcr.io/srp500005/electricity-bill-calculator:latest
```

Run it:

```bash
docker run --rm -it ghcr.io/srp500005/electricity-bill-calculator:latest
```

Private packages require authentication with an account that has permission to read the package.

## CI/CD Pipeline

The workflow runs automatically on pushes and pull requests.

| Job | Action |
|---|---|
| test | Install test dependencies and run pytest |
| build | Build the Docker image and check a calculation inside the container |
| publish | Build and upload Docker images to GHCR after successful checks on main |

If tests fail, the build and publish jobs are skipped.

Publishing runs only for pushes to the main branch. Images receive two tags:

- `latest`: the latest successfully published version.
- Commit SHA: a version associated with the exact source commit.

Each job runs in a separate environment, so the publish job rebuilds the image before uploading it.

This project implements continuous delivery. It does not automatically deploy a running application to a server.

## What I Practiced

- Separating calculation logic from interactive input.
- Writing tests for expected results and invalid values.
- Using Git branches, commits, and remote repositories.
- Configuring automated workflows with GitHub Actions.
- Packaging a Python application with Docker.
- Checking application behavior inside a container.
- Publishing versioned container images.

## Author

Shravankumar Prajapati

GitHub: https://github.com/SRP500005
