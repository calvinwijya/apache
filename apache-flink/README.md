# Apache Flink Training

## :pushpin: Getting Started

Before starting, make sure to have Docker and Docker Compose installed:

  1. [Docker Desktop](https://docs.docker.com/get-docker/) (required)
  2. [Docker Compose](https://docs.docker.com/compose/install/#installation-scenarios) (required)


## :boom: Running the pipeline

**:warning: Before you get started, ensure that Docker Desktop is open and the Docker Daemon is running! :warning:**

**Run the following commands to start the pipeline:**

  ```bash
  make down
  # docker compose down --remove-orphans # same as `make down`

  make up
  # docker compose --env-file flink-env.env up --build --remove-orphans -d

  make job
  # docker compose exec -d jobmanager ./bin/flink run -py /opt/src/job start_job.py --pyFiles /opt/src

  # or you can do `make restart` it will just run make down and up
  make restart
  ```

