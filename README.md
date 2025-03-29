# sw_da_kubernetes  

## 🚀 Kubernetes Flask Web Application  
A scalable Flask web application deployed on Kubernetes with auto-scaling capabilities.  

---

## 📂 Repository Structure  

```
sw_da/
├── k8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── hpa.yaml
│   └── service.yaml
├── templates/
│   ├── 404.html
│   ├── 500.html
│   ├── about.html
│   └── index.html
├── Dockerfile
├── app.py
└── requirements.txt
```

---

## 🛠 Deployment Guide  

### ⚡ Windows Users  

#### **1⃣ Install Docker Desktop**  
Download and install Docker from [docker.com](https://www.docker.com/products/docker-desktop).  

#### **2⃣ Install Minikube**  
```powershell
Invoke-WebRequest -Uri "https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe" -OutFile "minikube.exe"
Move-Item "minikube.exe" -Destination "C:\Windows\System32\" -Force
```

#### **3⃣ Install kubectl**  
```powershell
Invoke-WebRequest -Uri "https://dl.k8s.io/release/v1.28.0/bin/windows/amd64/kubectl.exe" -OutFile "kubectl.exe"
Move-Item "kubectl.exe" -Destination "C:\Windows\System32\" -Force
```

#### **4⃣ Start the Minikube Cluster**  
```powershell
minikube start --driver=docker --memory=4000mb --cpus=2
```

#### **5⃣ Deploy the Application**  
```powershell
cd sw_da
docker build -t flask-k8s-app .
kubectl apply -f k8s/
```

---

### 🐧 Ubuntu Users  

#### **1⃣ Install Dependencies**  
```bash
sudo apt update && sudo apt install -y docker.io curl
```

#### **2⃣ Configure Docker**  
```bash
sudo usermod -aG docker $USER
newgrp docker
```

#### **3⃣ Install Minikube**  
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

#### **4⃣ Install kubectl**  
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```

#### **5⃣ Start the Minikube Cluster**  
```bash
minikube start --driver=docker --memory=4000mb --cpus=2
```

#### **6⃣ Deploy the Application**  
```bash
cd sw_da
docker build -t flask-k8s-app .
kubectl apply -f k8s/
```

#### **7⃣ Enable Metrics Server (For Auto-Scaling)**  
```bash
minikube addons enable metrics-server
```

---

## ✅ Verification  

#### **Check Deployed Components**  
```bash
kubectl get all
```

#### **Get the Application URL**  
```bash
minikube service flask-service --url
```

---

## 🛡 Cleanup  

#### **Delete Minikube Cluster and Free Up Space**  
```bash
minikube delete
docker system prune -a -f
```

---

### 📌 Notes:
- Ensure **Docker is running** before starting Minikube.
- Minikube may require **VT-x/AMD-v enabled** in BIOS.
- If `kubectl get all` shows errors, restart the cluster:  
  ```bash
  minikube stop && minikube start
  ```

---
