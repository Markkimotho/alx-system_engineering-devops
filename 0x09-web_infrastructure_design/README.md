# 0x09. Web infrastructure design

`0. Simple web stack`


**What is a server?**
A server is a computer(physical or virtual) that contains information which is provided upon request by another computer called a "Client"

**Web Server**
**Role:** A Web Server is a program that handles HTTP requests from clients(usually web browsers) and serves or responds with HTML pages along with other object files embedded within them (e.g. image files).
**Application Server**
**Role:** However, some services not offered by the web server like Transaction Processing, API response or any other dynamic content are handled by the Application Server.

**What is DNS?**
DNS is a distributed database that is used to match a domain name to its corresponding IP Address.
For example; when you type www.google.com, a lookup/search is performed across this distributed database to find the corresponding address, which the browser then uses to find the server and request from it the information that is desired. 

In this example, we have www.foobar.com typed to the web browser. A DNS lookup is perfomed and the IP address (8.8.8.8) is returned. Then, the browser follows that address to find the server where the information it wants is located.

**Role Of the Domain Name.**
It is easier for human beings to remember names than a series of numbers. It is as simple as that.

**What type of DNS record www is in www.foobar.com**

The "www" in www.foobar.com is typically used as a subdomain, and is represented by a DNS record type called "CNAME"(Canonical Name) record.

CNAME is a record type that maps an alias of nickname to the canonical or true domain. In this scenario, the "www" is an alias for the main domain "foobar.com"
The CNAME record for the "www" subdomain typically points to the hostname of the web server that is hosting the website. For example, the CNAME record for "www.foobar.com" may point to "webserver.foobar.com".

When a user enters "www.foobar.com" in their web browser, the browser sends a DNS query to resolve the domain name to an IP address. The DNS server then returns the IP address associated with the CNAME record, which points to the web server that is hosting the website.

Overall, the "www" in "www.foobar.com" is typically represented by a CNAME record, which maps the subdomain to the canonical domain name and allows users to access the website using a human-readable alias.

**Role of the Database:** 
**What is a database?:** It is an organized store of data. The essense of databases is to store, manage, and retrieve data in a controlled and secure way. These are the advantages that set databases apart from other data storing methods like flat files.

In this case, we used the relational database MySQL. 

### Issues with this Infrastructure

### SPOF (Single Point Of Failure)

There are several **SPOFs(Single Point of Failure)** in this infrastructure. This implies that when a link or resource(i.e. database) is in one way or the other disconnected or removed, the request message might fail to arrive at the server or the response message might fail to arrive at the client. 

### Downtime when maintenance needed

When new code is added or written, the web server has to be restarted so that the changes can reflect. Since we have only one physical server to attend to a client(s), a downtime  will be experienced for as long as the server needs to restart to be updated with new changes. 
This problem thus demands replica server that can be able to attend to clients while the other server updates.

### Scale

The goal of scaling is to ensure that the system or application can handle increasing levels of traffic or workload, while maintaining performance and reliability. However, our current infrastructure isn't designed to handle heavy traffic. Say, we increase the number of requests to the www.foobar.com server, or we get more clients that want the data from the server. Our server might not withstand the "pressure"; the traffic might to too much for it's resources to handle. Therefore, the server will either slow down in it's response rate, cause some data collisions or might even crash. Needless to say, the Infrastructue is efficient for critical service provision.

`1. Distributed web infrastructure`

Additions to our infrastructure:
* 1 load-balancer (HAproxy)
* 2 Servers with similar implementations as the one task 0 : `0. Simple web stack`

### Load Balancer.
**Role:** A load balancer is a device or software is fundamentally used to efficiently and evenly distribute traffic across multiple servers or nodes, so that no single server is overwhelmed or overloaded with requests.

**Distribution Algorithm load balancer is configured with and how it works.**
The load balancer in use is HAproxy and it uses the Round Robin (the most commonly used load balancer algorithm). Requests are distributed across the group of servers sequentially. Request 1 is directed to server 1, request 2 to server 2, and so forth.

**Active-Active or Active-Passive setup, explain the difference between both.**
an active-active setup distributes traffic across multiple actively serving servers or instances, while an active-passive setup uses multiple servers but only one actively serves traffic at a time, with the other servers on standby. 

### Servers.
**Role:** These additional servers will serve the clients requests. The choice of server will depend on the load balancer--the algorithms it's configured with, the preferred setup(active-active or active-passive) and the configuration of the servers(master-replica) 


How a database Primary-Replica (Master-Slave) cluster works
A primary-replica (master-slave) cluster is a configuration of multiple database servers where one server acts as the primary or master node, while one or more servers act as replicas or slave nodes. The primary node serves as the primary source of data, and all writes and updates are made to this node. The replicas, on the other hand, are kept in sync with the primary by replicating the data from the primary node.

Difference between the Primary node and the Replica node in regard to the application
The primary node handles write requests and manages replication, while the replica nodes provide read scalability and redundancy.

## ISSUES WITH THIS INFRASTRUCTURE.

**SPOF**
**Security Issues(No Firewall)**
**No Monitoring**


`2. Secured and monitored web infrastructure`

Additions to our infrastructure:

* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)
	
### Firewalls
**Role:** 

## 1 SSL certificate to serve www.foobar.com over HTTPS
**Role:**

## 3 monitoring clients (data collector for Sumologic or other monitoring services)
**Role:**
---
## MONITORING
---
System monitoring is the tracking of its metrics to ensure that it is doing what it was set out and designed to do.

In a computer system(of client-server or peer-to-peer architecture), there is two types of approaches to monitoring the performance and availabilty of the system; Application and Server monitoring

### Application Monitoring
Application monitoring focuses on tracking the performance and behavior of individual applications running on a system. Some of the metrics that are observed are:

* Response time of the app
* Application's Errors and Exceptions
* Application's dependencies and Resource Utilization
* Application's logs

Application monitoring can help identify and diagnose issues such as **slow response times**, **bottlenecks**, and **errors within an application**, and can **provide insights into how the application is being used**.

### Server Monitoring
On the hand, Server Monitoring focuses on tracking the overall performance of the server or infrastructure hosting the application. Some of the metrics observed are:

* CPU Usage
* Disk Space Utilization
* Memory Usage
* Network traffic 
* & other system-level metrics.

Server monitoring can help identify issues such as **hardware failures**, **network connectivity problems**, and **system-level bottlenecks**, and **can provide insights into how the infrastructure is being used**.

In summary, application monitoring focuses on individual application performance and behavior, while server monitoring focuses on the health and performance of the underlying infrastructure hosting the application. Both types of monitoring are important for maintaining the availability, reliability, and performance of a system.


Explain what to do if you want to monitor your web server QPS



## ISSUES WITH THIS INFRASTRUCTURE.

Why terminating SSL at the load balancer level is an issue
Why having only one MySQL server capable of accepting writes is an issue
Why having servers with all the same components (database, web server and application server) might be a problem

`3-scale_up`









