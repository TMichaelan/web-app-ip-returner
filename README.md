# web-app-ip-returner

## ✨ Download

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

Clone the repository:
```bash
git clone https://github.com/TMichaelan/web-app-ip-returner.git
```
> 👉 **Step 2** - Navigate to the project directory:

```bash
git cd web-app-ip-returner
```

<br>

## ✨ Docker build 

To build and run the web application, follow these steps:


> 👉 **Step 1** - Build the Docker image:
```bash
docker build -t <image-name>:latest .
```
or

```bash
docker-compose up --build 
```

> 👉 **Step 2** - Run the Docker container:
```bash
docker run -p 5000:80 <image-name>:latest
```
example:
```bash
docker run -p 5000:80 web-app-ip-returner:latest
```


> 👉 **Step 3** - Check if the application is running by visiting http://localhost:5000 (or your port) in your web browser. You should see the IP address of your machine.

<br>

## ✨ Upload docker image to Docker Hub
<br>

> 👉 **Step 1** - Follow the steps from  <b>Docker build</b> section

<br>

> 👉 **Step 2** - Create repository on https://hub.docker.com/  

It would be like "your-name/repository-name"

<br>

> 👉 **Step 3** - Rename your docker image using:
```bash
docker tag <image-name>:latest <your-name>/<repository-name>:latest
```

<br>

> 👉 **Step 4** - Log in to DockerHub using:
```bash
docker login
```

<br>

> 👉 **Step 5** - Push your Docker image to the repository:
```bash
docker push <your-name>/<image-name>:latest
```

<br>

> 👉 **Step 6 (Optional)** - Test the Docker image:
```bash
docker run -it -p 5000:5000 <your-name>/<image-name>:latest
```
visit http://localhost:5000 (or your port)


## ✨ Build Kubernetes Cluster

### You should have the following programs installed:
1. Minikube - https://kubernetes.io/docs/tasks/tools/#minikube
2. kubectl - https://kubernetes.io/docs/tasks/tools/#kubectl

Install them and run the following command to start the cluster:
```bash
minikube start
```

> 👉 **Step 1** - Deploy the application to a Kubernetes cluster:

To deploy the application to a Kubernetes cluster, you need to create a deployment file. Here's an example:

```bash
apiVersion: v1
kind: Pod
metadata:
  name: web-app-ip-returner
spec:
  containers:
  - name: web-app-ip-returner
    image: michaelantt/k8sapp:latest
    ports:
    - containerPort: 5000
    livenessProbe:
      httpGet:
        path: /
        port: 5000
      initialDelaySeconds: 10
      periodSeconds: 10
      timeoutSeconds: 1
```
Save the file with a .yml extension, for example web-app-ip-returner-deployment.yml.

<b>!!! My docker hub name and repository name--> <i>michaelantt/k8sapp:latest</i> </b>


> 👉 **Step 2** - Apply the deployment file:
```bash
kubectl apply -f web-app-ip-returner-deployment.yml
```

### Dev Hints (Optional):

kubectl apply -f web-app-ip-returner.yml

kubectl expose deployment web-app-ip-returner --type=LoadBalancer --port=5000

kubectl get service web-app-ip-returner

kubectl get pods

kubectl run ip-returner --generator=run-pod/v1 --image=web-app-ip-returner:latest --port=80

kubectl create -f web-app-ip-returner.yml

minikube start

minikube stop

minikube delete

docker build -t ip-returner .

docker run -p 5000:5000 ip-returner


docker run -it -p 5000:5000 michaelantt/k8sapp

docker rmi <image-id> -f

kubectl get nodes

kubectl get pods

kubectl describe pod <pod-name>

kubectl exec <pod-name> date

kubectl exec -it <pod-name> sh

kubectl logs <pod-name>

kubectl port-forward <pod-name> 5000:5000

kubectl port-forward <pod-name> 5000:80

kubectl delete -f <file>.yml