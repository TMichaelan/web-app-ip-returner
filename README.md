# web-app-ip-returner

## ✨ Build

To build and run the web application, follow these steps:

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

Clone the repository:
```bash
git clone https://github.com/TMichaelan/web-app-ip-returner.git
```

> 👉 **Step 2** - Navigate to the project directory:
```bash
git cd web-app-ip-returner
```

> 👉 **Step 3** - Build the Docker image:
```bash
docker build -t web-app-ip-returner:latest .
```
or

```bash
docker-compose up --build 
```

> 👉 **Step 4** - Run the Docker container:
```bash
docker run -p 5000:80 web-app-ip-returner:latest
```

> 👉 **Step 5** - Check if the application is running by visiting http://localhost:5000 in your web browser. You should see the IP address of your machine.

> 👉 **Step 6** - Deploy the application to a Kubernetes cluster:

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

> 👉 **Step 7** - Apply the deployment file:
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