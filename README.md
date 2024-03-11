# k8sisfun Project

Welcome to the k8sisfun project! This repository is part of a larger project.

## Repositories

- [API Service Repository](https://github.com/Nivrin/k8sIsFun-APIService)
- [Data Service Repository](https://github.com/Nivrin/k8sIsFun-DataService)
- [Simple Front Repository](https://github.com/Nivrin/k8sIsFun-SimpleFront)

## Architecture

![Architecture](images/architecture.JPG)

# SimpleFront Application Documentation

Welcome to the documentation for my front-end application deployed on Kubernetes using Streamlit.

## Introduction

This repository contains the source code and deployment configurations for our front-end application. The application serves as the interface for accessing data related to state codes and names. It provides two main functionalities: converting state codes to state names and vice versa.

## Deployment

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Build the Docker image:

    ```bash
    docker build -t gcr.io/${PROJECT_ID}/front_app:v1 ..
    ```
4. push the Docker image:

    ```bash
    docker push gcr.io/${PROJECT_ID}/data_service:v1
    ```
 5. Create a container cluster (if you haven't already done so)
 ```bash
    gcloud container clusters create <name> --num-nodes=1 
    ```
6. Apply the Kubernetes service configuration:

    ```bash
    kubectl apply -f manifests/front_app-service.yaml
    ```

7. Apply the Kubernetes deployment configuration:

    ```bash
    kubectl apply -f manifests/front_app-deployment.yaml
    ```

## Continuous Integration/Continuous Deployment (CI/CD)

We use GitHub Actions for CI/CD. The workflow defined in the `google.yml` file automates the building, publishing, and deploying processes.
