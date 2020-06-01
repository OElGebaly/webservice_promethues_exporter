# Python Flask application exports metrics to Prometheus and Grafana

## **Python Applications:**

 **1. webapp** : is a python flask app the runs with 4 different endpoints each with different response time `(/ep_one,/ep_two,/ep_three,/ep_four)` plus one more endpoint `/error` that always return error , application uses the **"prometheus_flask_exporter"** libraries and objects to expose a 6th end points `/metrics` export prometheus metrics, see code files under /src/webapp.
 
 **2. requests_generator:** a python application that randomly generates requests to the webapp 5 endopoints , see codefiles under /src/request-generator.

 
## **Prometheus Server:**

a Prometheus server that runs into a kubernetes deployment with a scrapping job to export metrics from the webapp endpoint `/metrics` , a scrapping job is created under the prometheus.yaml file 

    - job_name: 'flaskapp'
      static_configs:
        - targets: ['webapp:5000'] 
 
## **Grafana instance:**

a Grafana instance is to get a the valid promethues metrics via a created Prometheus datasource pointing to the running Prometheus server , a grafana dashboard is also created with the below metrics:

 **- Number of Requests per second**

Number of successful Flask requests per second. Shown per endpoint.

 **- Errors per second**

Number of failed (non HTTP 200) responses per second.

 **- Total requests**

The total number of requests measured over two minute intervals. Shown per HTTP response status code.

 **- Average response time**

The average response time measured over 2 minutes intervals for successful requests. Shown per path.

 **- Requests under 250ms**

The percentage of successful requests finished within 1/4 second. Shown per path.

 **- Request duration**

The 50th percentile of request durations over the last 2 minutes. In other words, half of the requests finish in (min/max/avg) these times. Shown per path.

 **- Memory usage**

The memory usage of the Flask app. Based on data from the underlying Prometheus client library.

 **- CPU usage**

The CPU usage of the Flask app as measured over 2 minutes intervals. Based on data from the underlying Prometheus client library.

![grafana](https://github.com/OElGebaly/webservice_promethues_exporter/blob/master/k8s/grafana/grafana.png)


## Kubernetes Components
![enter image description here](https://github.com/OElGebaly/webservice_promethues_exporter/blob/master/K8s_Diagram.jpg)

1. **Minikube Cluster**
2. **Namespace: Monitoring**
3. **Deployment: Webapp** , it should contain a POD where the python application webapp is running. 
4. **Deployment: Requests-Generator** , it should contain a POD where the python application requests-generator is running.
5. **Service: Webapp:**, used by both the **Requests-Generator** and **Promethues** to obtain the endpoints.
6. **Deployment: Prometheus**, will deploy Prometheus server and needed configurations.
7. **Deployment: Grafana**, will deploy Grafana instance and needed configurations.
8. **Service: Prometheus**, used by Grafana to obtain metrics.
9. **Service: Grafana**, used to obtain browser access to grafana.

## Deployment Steps

 1. start a new [minikube](https://github.com/kubernetes/minikube) cluster 
 2. deploy Prometheus server
	```
	kubectl apply -f k8s/promethues/prometheus-deployment.yaml 
	kubectl apply -f k8s/promethues/prometheus-service.yaml
	```
 3. Deploy Applications
	 ```
		kubectl apply -f k8s/webapp/webapp-deployment.yaml 
		kubectl apply -f k8s/webapp/webapp-service.yaml
	```
 4. Deploy Grafana
	 ```
		kubectl apply -f k8s/grafana/grafana-datasource-config.yaml 
		kubectl apply -f k8s/grafana/grafana-deployment.yaml
		kubectl apply -f k8s/grafana/grafana-service.yaml
	```
 5. ensure all pods are up and running
	 ```
	 $ kubectl get pods -n monitoring
	 
	NAME                                  READY   STATUS    RESTARTS   AGE
	grafana-xxx-xxx               1/1     Running   0          8h
	prometheus-xxx-xxx           1/1     Running   0          156m
	requests-generator-xxx-xxx   1/1     Running   0          3h
	webapp-xxx-xxx               1/1     Running   0          3h1m
	```
 6. list all existing services
	 ```
	$ minikube service list

	|-------------|--------------------|--------------|-----------------------------|
	|  NAMESPACE  |        NAME        | TARGET PORT  |             URL             |
	|-------------|--------------------|--------------|-----------------------------|
	| default     | kubernetes         | No node port |
	| kube-system | kube-dns           | No node port |
	| monitoring  | grafana            |         3000 | http://xx.xx.xx.xx:32000 |
	| monitoring  | prometheus-service | No node port |
	| monitoring  | webapp             |         5000 | http://xx.xx.xx.xx:30100 |
	|-------------|--------------------|--------------|-----------------------------|
	```
 7. once all dine successfully , open grafana [http://localhost:32000/](http://localhost:32000/) , or use the URL as displayed from the above command right beside grafana, access credentials are (user: admin , password: admin) , and then you will be asked to set a new password.
 8. import new dashboard with the file `k8s/grafana/dashboard.json ` to display the above metrics.

