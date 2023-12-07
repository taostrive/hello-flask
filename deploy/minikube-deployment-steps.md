## How to deploy the application to a Minikube Kubernetes cluster

**Prerequisites:**

* A Kubernetes cluster created with Minikube must be running.

**Step 1: Enable Minikube's Local Container Registry**

1. Run the following command to enable the Minikube registry addon:

```bash
minikube addons enable registry
```

2. Start a container listening on port 5000 and forwarding traffic to the Minikube registry on the same port:

```bash
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
```

**Step 2: Clone the Application Repository**

1. Clone the application repository from GitHub:

```bash
git clone https://github.com/taostrive/hello-flask.git
```

**Step 3: Build and Tag the Docker Image**

1. Change directory to the `hello-flask` repository:

```bash
cd hello-flask
```

2. Build the Docker image with the tag `1207`:

```bash
docker build -t hello-flask:1207 .
```

3. Tag the image for pushing to the Minikube registry:

```bash
docker tag hello-flask:1207 localhost:5000/myimage:1207
```

**Step 4: Push the Image to Minikube's Registry**

1. Push the image to the Minikube registry:

```bash
docker push localhost:5000/myimage:1207
```

**Step 5: Deploy the Application with Helm**

1. Use Helm to upgrade or install the application with the `deploy/helm` chart:

```bash
helm upgrade --install my-hello-flask ./deploy/helm --set image.repository=localhost:5000/myimage --set image.tag=1207
```

**Step 6: Port Forward the Application Service**

1. Forward the application's service port (5001) to a local port (5001) for access:

```bash
kubectl port-forward svc/my-hello-flask-app 5001:5001
```

**Step 7: Verify Application Accessibility**

1. Use `curl` to send requests and verify the application's response:

```bash
curl -v http://localhost:5001
curl -v http://localhost:5001/health
```
