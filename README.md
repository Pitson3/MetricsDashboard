**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

A. *monthly uptime*
- Total time that the service is often down during the month
- Total time that the service is available to the users during the month

B. *request response time*
- The maximum number of time that the user waits for the data to be displayed on the frontend application
- The minimum number of time that the backend API returns data to the client application
- The average time that it takes for the request to be processed by the backend application

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

A. *Uptime*
This covers the total amount of time that a service is available to the customer. In our case, the service should mostly be up and running, and if the service is down then the reasons must be investigated and mitigated based on the SLIs so as to ensure that we always offer our customer the best service for the projected service level objectives(SLOs) in on a monthly uptime basis.

B. *Error Rate*
This encompasses the intensity at which the service fails in a specific time. That being said, it is crucial that all errors with  our services are investigated and dealt with accordingly so as to esnure that our service is operating with minimal faults or fast recovery from errors.

C. *Traffic*
This includes the total amount of requests that are made to the service in a specific time. This should also cover all concurrent requests from various users per a specific time. In our case, it will be capture to the amount of traffic so that we can easily sense on how the service is able to couple up with issues inline with service's traffic overload.

D. *Network Usage*
This covers the amount or percentage of network bandwidth that a service requires in a specific time so as to fully to handle all of the request payload. This is is crucial because sometimes network performance can be a barrier or booster to the performance level of our service.

E. *Latency*
This covers the total time to process a request and offers the right feedback to the customer or client. It is therefore crucial that we measure the latency so that our customers are not frustrated due to long waiting time for the requests to be fully processed.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
