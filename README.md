**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

![img_1][./answer-img/pods_svc_all_components.png]

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![img_2][./answer-img/grafana_homepage.png]

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![img_3][./answer-img/basic-dashboard.png]

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

- The Service Level Objective(SLO) is the expected or overall projected performance goals in specific timeframe whereas the Service Level Indicator(SLI) defines or records the achieved performance level against the proposed SLO. Incase of the monthly uptime, the SLI would be a recording of the 90% of the service uptime against the expected SLO of 99.9% in a month. Meanwhile, for the request response time; the SLI will be an achieved average response time of 95ms against the expected SLO of 100ms in a specific month.
 
## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

A. *Uptime*
- This covers the total amount of time that a service is available to the customer. In our case, the service should mostly be up and running, and if the service is down then the reasons must be investigated and mitigated based on the SLIs so as to ensure that we always offer our customer the best service for the projected service level objectives(SLOs) in on a monthly uptime basis.

B. *Error Rate*
- This encompasses the intensity at which the service fails in a specific time. That being said, it is crucial that all errors with  our services are investigated and dealt with accordingly so as to esnure that our service is operating with minimal faults or fast recovery from errors.

C. *Traffic*
- This includes the total amount of requests that are made to the service in a specific time. This should also cover all concurrent requests from various users per a specific time. In our case, it will be capture to the amount of traffic so that we can easily sense on how the service is able to couple up with issues inline with service's traffic overload.

D. *Network Usage*
- This covers the amount or percentage of network bandwidth that a service requires in a specific time so as to fully to handle all of the request payload. This is is crucial because sometimes network performance can be a barrier or booster to the performance level of our service.

E. *Latency*
- This covers the total time to process a request and offers the right feedback to the customer or client. It is therefore crucial that we measure the latency so that our customers are not frustrated due to long waiting time for the requests to be fully processed.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![img_4][./answer-img/uptime_errors.png]

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

![img_5][./answer-img/backend_jaegar_trace.png]

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![img_6][./answer-img/Jaegar_Trace.png]

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: Backend Error for the /star Endpoint

Date: 16th December, 2021

Subject: /Star Endpoint Failed Due to MongoDB Issues

Affected Area: Backend-Service(API)

Severity: Critical

Description: An Internal Server Error is encountered on a post request for the /star endpoint. The issue is triggered by the inaccessible MongoDB Server/Database on our local kubernetes cluster. Hence, MongoDB will have to be installed and configured on our local cluster in order to be recording successful post requests on the /star endpoint.


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

- Uptime: The application/service should be up and running for atleast 99.9% of the time on monthly basis.
- Latency: The average request response time should not exceed 15ms on monthly basis.
- Error Rate: The 20X status codes should be recorded for not less than 99.9% of the total requests whereas the 50X and 40X status codes should be recorded for less than 0.1% on all of the http requests made in month.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

- Resource Utilization: The amount of CPU, memory and other system resources used by a service or pod.
- Error Rate: The recorded errors per unit time(mostly seconds). This covers the 40X and 50X errors
- Uptime: The total time that a service is available for usage
- Latency: The requests response time

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![img_7][./answer-img/FinalDashboard1.png]

![img_8][./answer-img/FinalDashboard2.png]

- Uptime: Average time that the services are up and running 
- Errors: The http 40X and 50X errors encountered by the services
- Latency: Average http requests per second
- CPU Usage: The amount of cpu used by continers in a second
- Memory Usage: The amount of memory used by the containers in a second


