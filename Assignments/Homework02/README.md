# Homework 02

## Description  
This folder contains the assignments for Week 3 & 4. The tasks focus on isolating our work from our development environment through a process called containerization.

## Contents  
1. **Writer** - Generates a data file (`data.txt`)
2. **Computer** - Processes `data.txt` and outputs `results.txt`
3. **Webserver** - Serves `results.txt` via a simple HTTP server on port `8000`
---
### 📦 Building the Docker Images  
To build the images separately for each service, run:
1. docker build -t writer-image -f dockerWriter
2. docker build -t computer-image -f dockerComputer
3. docker build -t webserver-image -f dockerHTML
---
## 🏃🏻‍♂️ Running Each Service Individually Without Docker Compose
### Run Writer
docker run -v $PWD/data:/data --rm -it writer-image
### Run Computer
docker run -v $PWD/data:/data" --rm -it computer-image
### Run Webserver
docker run -v $PWD/data:/data -p 8000:8000 webserver-image
---
## 🏃🏻‍♂️ Running Everything with Docker Compose  
### Run Writer
docker compose run writer
### Run Computer
docker compose run computer
### Run Webserver
docker compose run webserver
    or
## 🛠️ To build and start all three together:
docker compose up --build -d
