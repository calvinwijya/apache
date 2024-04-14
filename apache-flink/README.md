# Apache Flink Training

## :pushpin: Getting Started

Before starting, make sure to have Docker and Docker Compose installed:

  1. [Docker Desktop](https://docs.docker.com/get-docker/) (required)
  2. [Docker Compose](https://docs.docker.com/compose/install/#installation-scenarios) (required)


## :boom: Running the pipeline

**:warning: Before you get started, ensure that Docker Desktop is open and the Docker Daemon is running! :warning:**


:information_source: To see all the make commands that're available and what they do, run:

  ```bash
  make help
  ```


**Run the following commands to start the pipeline:**

  ```bash
  make down
  # docker compose down --remove-orphans # same as `make down`

  make up
  # docker compose --env-file flink-env.env up --build --remove-orphans -d

  make job
  # docker compose exec -d jobmanager ./bin/flink run -py /opt/src/job start_job.py --pyFiles /opt/src

  make restart
  # you can do `make restart` it will just run make down and up
  ```


**Now you should be able to see the job running in the Flink UI at [http://localhost:8081/](http://localhost:8081/).**

**In a separate terminal, connect to the PostgreSQL service using the PostgreSQL CLI:**

  ```bash
  make psql
  # docker exec -it pyflink-postgres psql -U postgres -d postgres -p 5632
  ```


## :broom: Clean up

**When you're done, make sure to terminate the running terminals, stop the running containers, and clean up any unused resources:**
    
```bash
make down

# Or:
docker compose down --remove-orphans
```

**If you want to cancel any running Flink jobs without stopping the Flink cluster, you can use the following command:**

```bash
make cancel
```

> *This command automatically retrieves and cancels all running Flink jobs. If you don't have Make, you can simply cancel the jobs in the Flink UI.*
>
> *If you want to manually cancel a job with specific job id you can run this command*
> 
> ```bash
> docker compose exec -d jobmanager ./bin/flink cancel <JOB_ID>
> ```
>
> *You can list flink job in case you don't want to check directly from the Flink UI*
>
> ```bash
> docker compose exec -d jobmanager ./bin/flink list -r
> ```
>

## System Diagram
TBD


### References
- https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/deployment/resource-providers/standalone/docker
