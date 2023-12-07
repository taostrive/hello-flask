## README

This document provides information about the simple Hello World application with two endpoints and its accompanying Docker image and CI/CD pipeline.

**Stack:**

* **Programming Language:** Python 3.9
* **Framework:** Flask
* **Testing framework:** pytest
* **Linter:** flake8
* **Docker:** Dockerfile
* **CI/CD:** Github Actions

**Solution and Decisions:**

**Endpoints:**

* The application exposes two endpoints:
    * `/`: Returns a JSON response with the message "Hello World".
    * `/health`: Checks the application's health and returns a success or failure response with details.

**Docker:**

* A Dockerfile builds a Docker image containing the application and its dependencies. This allows for easy deployment and portability.

**CI/CD:**

* A Github Actions workflow automates code checks (linting and tests), Docker container builds, and Docker image pushes to Docker Hub. This ensures consistent quality and deployment practices.

**Decisions:**

* Flask was chosen as the web framework due to its simplicity and ease of use.
* pytest was selected for unit testing due to its wide use in Python ecosystem.
* flake8 was chosen for linting to enforce code style and quality.
* Docker was used for containerization to ensure consistent runtime environments.
* Github Actions was chosen for CI/CD due to its integration with Github and ease of configuration.

**Further Development:**

* Switch packaging tool/dependencies management from Pipenv to Poetry.
* Use a production WSGI server for production deployments.
* Enable TLS.
* Implement additional API endpoints.
* Improve the application's health check logic.
* Add more unit and integration tests.
* Configure logging and monitoring for the application.
* Deploy the application to a cloud platform.

