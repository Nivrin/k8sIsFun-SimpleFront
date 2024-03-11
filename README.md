# SimpleFront Application Documentation

Welcome to the documentation for our front-end application deployed on Kubernetes using Streamlit.

## Introduction

This repository contains the source code and deployment configurations for our front-end application. The application serves as the interface for accessing data related to state codes and names. It provides two main functionalities: converting state codes to state names and vice versa.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Build the Docker image:

    ```bash
    docker build -t front-app .
    ```

## Running the Application Locally

To run the application locally, execute the following command:

```bash
docker run -p 8501:8501 front-app
