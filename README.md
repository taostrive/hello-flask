## README

This document provides information about the simple Hello World application with two endpoints and its accompanying Docker image and CI/CD pipeline.

**Stack:**

* **Programming Language:** Python 3.9
* **Framework:** Flask
* **Testing framework:** pytest
* **Linter:** flake8
* **Docker:** Dockerfile
* **CI/CD:** Github Actions
* **Kubernetes support:** Deploy application to kubernetes using helm chart

**Solution and Decisions:**

**Endpoints:**

* The application exposes two endpoints:
    * `/`: Returns a JSON response with the message "Hello World".
    * `/health`: Checks the application's health and returns a success or failure response with details.

**Docker:**

* A Dockerfile builds a Docker image containing the application and its dependencies. This allows for easy deployment and portability.

**CI/CD:**

* A Github Actions workflow automates code checks (linting and tests), Dockerfile scan and Docker container builds and image scans, and Docker image pushes to Docker Hub(skipped currently). This ensures consistent quality and deployment practices.

**Kubernetes support:** 

* The Helm chart provided in the `deploy` directory allows for deploying this application to any Kubernetes environment. Local development and testing of applications intended for deployment in a Kubernetes cluster can be significantly facilitated and accelerated by utilizing tools like Minikube, KIND, or Colima. This enables developers to work with a local Kubernetes cluster and test their applications without requiring access to a remote cluster.

To deploy and test this application in a local Kubernetes cluster created via Minikube on a Linux machine, follow the steps outlined [here](deploy/minikube-deployment-steps.md).



**Decisions:**

* Flask was chosen as the web framework due to its simplicity and ease of use.
* pytest was selected for unit testing due to its wide use in Python ecosystem.
* flake8 was chosen for linting to enforce code style and quality.
* Docker was used for containerization to ensure consistent runtime environments.
* Github Actions was chosen for CI/CD due to its integration with Github and ease of configuration.
* Helm charts was used to deploying this application to any Kubernetes cluster as it seamlessly integrate with CI/CD pipelines, allowing automated and consistent application deployments.

**Further Development:**

* Enhance the GitHub Actions CI/CD pipeline to deploy the Helm chart into a KIND cluster. 
* Switch packaging tool/dependencies management from Pipenv to Poetry.
* Use a production WSGI server for production deployments.
* Enable Authetication, Authorization and TLS.
* Implement additional API endpoints.
* Improve the application's health check logic.
* Add more unit and integration tests.
* Configure logging and monitoring for the application.
* Support deploying the application to a cloud Kubernetes cluster by enhancing the helm chart, e.g. enable accessing to the application via an ingress resource.

