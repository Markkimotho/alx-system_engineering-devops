# 0x09. Web infrastructure design

## `0. Simple web stack`

### Specifics of this infrastructure: 

#### What is a server:

A server is a computer(physical or virtual) that contains information which is provided upon request by another computer called a "Client"

#### What is the role of the domain name



#### What is DNS?:

DNS is a distributed database that is used to match a domain name to its corresponding IP Address.
For example; when you type www.google.com, a lookup/search is performed across this distributed database to find the corresponding address, which the browser then uses to find the server and request from it the information that is desired. 
In this example, we have www.foobar.com typed to the web browser. A DNS lookup is perfomed and the IP address (8.8.8.8) is returned. Then, the browser follows that address to find the server where the information it wants is located.

#### Role Of the Domain Name:
It is easier for human beings to remember names than a series of numbers. It is as simple as that. Fundamentally the domain name is an alias for the IP address.­

#### What type of DNS record is "www"  in "www.foobar.com":
**Type A**

A DNS record is in the format : RR(name, value, type, ttl)

This record maps the domain to the IP address-- where name:domain name and value is IP Address which implies a record of type A

#### What is the role of:

* Web Server:

A Web Server is a program that handles HTTP requests from clients(usually web browsers) and serves or responds with HTML pages along with other object files embedded within them (e.g. image files).

* Application Server:

However, some services not offered by the web server like Transaction Processing, API response or any other dynamic content are handled by the Application Server.

* **What is the role of the database**

#### Database?:
It is an organized store of data. The essense of databases is to store, manage, and retrieve data in a controlled and secure way. These are the advantages that set databases apart from other data storing methods like flat files.

In this case, we used the relational database MySQL to store our data in tables from where they can be retrieved upon request. Relational database was the most preferred candidate because it allows CRUD opeartions. 

#### What is the server using to communicate with the computer of the user requesting the website

HTTP - A protocol that governs how servers and clients communicate.


### Issues with this Infrastructure

* **SPOF (Single Point Of Failure)**

There are several **SPOFs(Single Point of Failure)** in this infrastructure. This implies that when a link or resource(i.e. database) is in one way or the other disconnected or removed, the request message might fail to arrive at the server or the response message might fail to arrive at the client. 

* **Downtime when maintenance needed**

When new code is added or written, the web server has to be restarted so that the changes can reflect. Since we have only one physical server to attend to a client(s), a downtime will be experienced for as long as the server needs to restart to be updated with new changes. 
This problem thus demands replica server that can be able to attend to clients while the other server updates.
* **Scale challenges**

The goal of scaling is to ensure that the system or application can handle increasing levels of traffic or workload, while maintaining performance and reliability. However, our current infrastructure isn't designed to handle heavy traffic. Say, we increase the number of requests to the www.foobar.com server, or we get more clients that want the data from the server. Our server might not withstand the "pressure"; the traffic might to too much for it's resources to handle. Therefore, the server will either slow down in it's response rate, cause some data collisions or might even crash. Needless to say, the Infrastructue is efficient for critical service provision.


## `1. Distributed web infrastructure`

### Specifics of this infrastructure 
Additions to our infrastructure:
* 1 load-balancer (HAproxy)
* 2 Servers with similar implementations as the one task 0 : `0. Simple web stack`

#### Load Balancer.

* **Role:** A load balancer is a device or software that will be used to efficiently and evenly distribute traffic across multiple servers or nodes, so that no single server is overwhelmed or overloaded with requests.
#### Servers.

* **Role:** These additional servers will serve the clients requests and ultimately reduce the traffic to  one server that might stunt performance. The choice of server will depend on the load balancer--the algorithms it's configured with, the preferred setup(active-active or active-passive) and the configuration of the servers(master-replica) 

**What distribution algorithm your load balancer is configured with and how it works**

The load balancer in use is HAproxy and it uses the Round Robin (the most commonly used load balancer algorithm). Requests are distributed across the group of servers sequentially. Request 1 is directed to server 1, request 2 to server 2, and so forth.

**Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both**

an active-active setup distributes traffic across multiple actively serving servers or instances, while an active-passive setup uses multiple servers but only one actively serves traffic at a time, with the other servers on standby. 

**How a database Primary-Replica (Master-Slave) cluster works**

A primary-replica (master-slave) cluster is a configuration of multiple database servers where one server acts as the primary or master node, while one or more servers act as replicas or slave nodes. The primary node serves as the primary source of data, and all writes and updates are made to this node. The replicas, on the other hand, are kept in sync with the primary by replicating the data from the primary node.

**What is the difference between the Primary node and the Replica node in regard to the application**

The primary node handles write requests and manages replication, while the replica nodes provide read scalability and redundancy.


### Issues with this infrastructure
* **SPOF**

The Load Balancer is a single point for this infrastructure. If it went down during operation, then the rest of the servers will not recieve the request nor will the client get the response. Another SPOF is the database; if the database goes down then data will not be retrived. Utltimately, There are multiple SPOFs.

* **Security Issues(No Firewall)**

It is easy to pass unwanted traffic into the servers. For instance, a malicious party might use the load balancer to inject malware into the database in the servers through SQL injections or other hacking malpractices. No firewall means unwanted traffic can get into and out of the servers which is not good for the website owners not the clients. 

* **No Monitoring**

If not monitored systems can behave in undefined ways without notice, and when noticed they might results to costly debugging mechanisms. It will end up leading to losses because the services offered by the servers might seize or behave in peculiar ways. 


## `2. Secured and monitored web infrastructure`

### Specifics of this infrastructure 
Additions to our infrastructure:
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)

#### Firewalls
Secures our servers by filtering inbound or outbound traffic

#### SSL Certification
Secures TCP connection between the client and server to prevent attacks by hackers

#### Monitoring clients
Keeping tabs on the device it's monitoring to be able to know when a device is not working as it should so that the engineers can make repairs before more damage is done.


**What are firewalls for**

Firewalls are devices or software that are used to filter incoming or outgoing traffic. They offer a way of protecting devices from malicious attacks or preventing unwanted information into and out of the device.

**Why is the traffic served over HTTPS**

During the server-client communication, the TCP connection that enable this process communication might  be an avenue for malicious intent and attacks. The open ports are unprotected and might be used by hackers. To address this problem, a secure TCP connection ought to be established. This is enabled by SSL (Socket Layer Security) which was previously referred to as TLS (Transport Layer Security)

**What monitoring is used for**

System monitoring helps to ensure that a system is doing what it was set out and designed to do, and doing effectively and efficiently while at it.

**How the monitoring tool is collecting data**

A monitoring tool collects data from various sources such as logs, metrics, events, and traces, using methods such as agents, sensors, or APIs. The collected data is then processed to extract relevant information by filtering, aggregating, or transforming it. The processed data is stored in a database or data store using different storage technologies. The monitoring tool provides a user interface to view the collected data in the form of dashboards, charts, graphs, and other visualizations that provide insights into the system or network being monitored.

**Explain what to do if you want to monitor your web server QPS**
To monitor the QPS of a web server, you need to install a monitoring tool and agent on the server. The monitoring tool collects data and sends it to the monitoring agent. Then, you need to configure the monitoring tool to collect QPS data and set monitoring thresholds to trigger alerts when the QPS exceeds a certain limit. The monitoring tool's user interface can be used to monitor and analyze QPS data to identify trends and patterns, optimize server performance, and provide a better user experience.


### Issues with this infrastructure
* **Why terminating SSL at the load balancer level is an issue**

If SSL is terminated at the load balancer level, traffic between the load balancer and the web server is unencrypted, which can lead to data breaches. Compliance standards such as PCI DSS require SSL to be terminated at the web server level. Terminating SSL at the load balancer level can also impact performance and make troubleshooting SSL-related issues difficult. It is generally recommended to terminate SSL at the web server level to minimize risks and ensure compliance with relevant standards.

* **Why having only one MySQL server capable of accepting writes is an issue**
Having only one MySQL server capable of accepting writes can be an issue because it creates a single point of failure. If the MySQL server fails, the entire application that relies on it may also fail, leading to downtime and loss of revenue. Additionally, having only one write-capable MySQL server can limit scalability and performance because all write requests must go through a single server. This can result in slow response times, particularly during periods of high traffic or heavy write loads. To mitigate these issues, it is recommended to use a MySQL cluster or a master-slave replication setup to distribute the write load across multiple servers and provide fault tolerance and better performance.

* **Why having servers with all the same components (database, web server and application server) might be a problem**

Having servers with all the same components, such as database, web server, and application server, might be a problem because it can lead to a lack of diversity and increased risk of a single point of failure. If all servers have the same components, they may all be vulnerable to the same security threats or software bugs. If a software bug or security vulnerability is discovered, it may affect all servers and cause widespread downtime or data breaches. Additionally, if all servers have the same hardware and software configuration, they may all require the same patches or upgrades at the same time, which can lead to service interruptions or compatibility issues. To mitigate these risks, it is recommended to have a mix of server types and configurations, such as having different versions of operating systems or software, to provide diversity and reduce the risk of a single point of failure.

## `3-scale_up`

## Specifics of this infrastructure 

**Additions to the Infrastructure:**
* 1 Server 
* 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server

### Another Server

### Another Load Balancer configured as cluster with the other one

### Split components (web server, application server, database) with their own server

## Issues with this infrastructure










