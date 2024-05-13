minikube image load docker-lection-main-consumer
minikube image load docker-lection-main-producer

kubectl get svc
minikube service producer --url   #create a tunnel to the cluster