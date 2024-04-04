# Data OS

## Description

Data OS is a FastAPI based project that uses Kafka for messaging anb Zeebee for orchestration

This project contains several key components, such as tasks for handling specific operations, routers for directing
requests, and schemas for data validation and structure

## Installation

Clone the repository to your local machine.
Navigate to the project directory.
Install the dependencies.

```shell
poetry install
```

Run the application

```shell
uvicorn app.main:app
```

You can then access the apis at `http://localhost:8000/docs`.

## Camunda / Zeebee Setup

1. Clone https://github.com/camunda/camunda-platform
2. Run

```shell
docker compose -f docker-compose-core.yaml up
 ```

### Links

1. https://github.com/camunda/camunda-platform
2. https://docs.camunda.io/docs/next/self-managed/platform-deployment/helm-kubernetes/guides/local-kubernetes-cluster
3. https://docs.camunda.io/docs/next/self-managed/platform-deployment/overview/#development

## Contributing

We welcome contributions. Please open an issue first to discuss what you would like to change. Ensure to update tests as
appropriate.