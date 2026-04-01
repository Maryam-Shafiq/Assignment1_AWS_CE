# Assignment1_AWS_CE

## UniEvent – Cloud-Based Event Management System

### Assigment Overview

UniEvent is a cloud-hosted web application deployed on AWS that allows users to browse university events dynamically fetched from an external API.

---

### AWS Services Used

* Amazon EC2 – Hosting application servers
* Amazon S3 – Storing event images
* Amazon VPC – Network isolation
* Elastic Load Balancer – Traffic distribution
* IAM – Secure access management

---

### Architecture Design

* VPC with public and private subnets across multiple Availability Zones
* EC2 instances deployed in private subnets for security
* Load Balancer placed in public subnet
* S3 bucket used for storing event media
* IAM role attached to EC2 for secure S3 access

---

### System Workflow

1. User sends request via browser
2. Request goes to Load Balancer
3. Load Balancer forwards to EC2 instance
4. Application fetches event data from external API
5. Data processed and displayed to user
6. Event media stored in S3

---

### External API

A public API is used to fetch event data in JSON format.
This eliminates manual data entry and ensures dynamic content.

---

### Security Features

* Private subnets for backend servers
* Security groups controlling traffic
* IAM roles instead of hardcoded credentials

---

### Scalability & Fault Tolerance

* Multiple EC2 instances ensure availability
* Load Balancer distributes traffic
* System remains operational even if one instance fails

---

### Features

* Dynamic event fetching
* Cloud deployment on AWS
* Scalable and fault-tolerant design

---

### Conclusion

This project demonstrates a secure, scalable, and fault-tolerant cloud architecture using AWS services.

---
