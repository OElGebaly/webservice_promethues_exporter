# Python Flask application exports metrics to Prometheus and Grafana

## **Python Applications:**

 **1. webapp** : is a python flask app the runs with 5 different endpoints each with different response time `(/ep_one,/ep_two,/ep_three,/ep_four,/error )`, application uses the **"prometheus_flask_exporter"** libraries and objects to expose a 6th end points `/metrics` export prometheus metrics, see code files under /src/webapp.
 
 **2. requests_generator:** a python application that randomly generates requests to the webapp 5 endopoints , see codefiles under /src/request-generator.

