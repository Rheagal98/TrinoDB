# TrinoDB cluster - Docker Deployment

This project deploy a small TrinoDB cluster with Iceberg setup for experimenting and testing purpose

`#Trinodb`, `mysql`, `mongodb`


## Prerequisites

- Docker
- Docker Compose
- .env file (refer to .env.example)

## Setup 
For Local environment 

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/your-repository.git
   ```

2. Build and start the containers:

   ```shell
   docker-compose -f docker-compose.yaml up -d --build
   ```
