# sw_da_kubernetes
# Kubernetes Flask Web Application
A scalable Flask web application deployed on Kubernetes with auto-scaling capabilities.

## 📂 Repository Structure
sw_da/
├── k8s/ # Kubernetes manifests
│ ├── configmap.yaml # Environment configuration
│ ├── deployment.yaml # Application deployment
│ ├── hpa.yaml # Auto-scaling rules
│ └── service.yaml # Service exposure
├── templates/ # HTML templates
│ ├── 404.html # Error page
│ ├── 500.html # Server error page
│ ├── about.html # About page
│ └── index.html # Homepage
├── Dockerfile # Container configuration
├── app.py # Flask application
└── requirements.txt # Python dependencies

## Deployment guide 
## Windows Users
1. Install Prerequisites


## Ubuntu users
all commands to be executed in bash

1.Install Dependencies 
sudo apt update && sudo apt install -y docker.io curl
2.Configure Docker Permissions
sudo usermod -aG docker $USER
newgrp docker
3.Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
4. Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
5.Start Cluster
minikube start --driver=docker --memory=4000mb --cpus=2
6. Deploy Application
cd sw_da
docker build -t flask-k8s-app .
kubectl apply -f k8s/
7. Enable Metrics (for HPA)
minikube addons enable metrics-server
8. Access the App
minikube service flask-service --url
