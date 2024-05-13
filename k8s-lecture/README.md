Поставимо докер через [snap](https://github.com/docker-archive/docker-snap) чи [apt](https://docs.docker.com/engine/install/ubuntu/):
```
sudo snap install docker

sudo addgroup --system docker
sudo adduser $USER docker
newgrp docker

sudo snap disable docker
sudo snap enable docker
```
Встановимо [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/):
```
snap install kubectl --classic
```
Встановимо [minikube](https://kubernetes.io/uk/docs/tasks/tools/install-minikube/):
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
&& sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
Додамо ніштяків (якщо ще нема)
```
minikube addons list
minikube addons enable metrics-server
minikube addons enable dashboard
minikube dashboard 
```
Перевіромо чи все добре (API кластреа доступно через проксі `localhost:8001`)
```
kubectl proxy
http://localhost:8001/healthz
```
Щоб додати локальний регістрі: `minikube image load <image name>`