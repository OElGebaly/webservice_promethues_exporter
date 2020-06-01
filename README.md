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
