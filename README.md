# fpb-fantasy

This is a basketball fantasy web application built with Django. It allows users to create fantasy basketball teams and compete with others.

## Prerequisites

Before running the application, ensure that you have the following software installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started
To run the project locally, you can use Docker Compose, which will set up a PostgreSQL database along with Django app container.


1. You need to create an .env file in the project directory and populated with the appropriate values for the database configuration.

   ```bash
    DB_NAME=<database_name>
    DB_USER=<database_username>
    DB_PASSWORD=<database_password>
    DB_HOST=<database_host>
    DB_PORT=<database_port>

_Note: If using the docker-compose config the **`db_host`** should be **`db`**_

2. Build and start the containers by running the following command in the project's root directory:

   ```bash
   docker-compose build && docker-compose up
   ```
    This command will build the Docker images and start the containers defined in the docker-compose.yml file.
    The PostgreSQL database container will be initialized and connected to the project.

## Usage
Once the containers are up and running, you can access your application at _**http://localhost:8000**_ in your browser.

To stop and remove the containers, you can use the following command:
   ```bash
    docker-compose down
   ```
If you want to inspect the individual containers and access their shells, you can use the -it /bin/bash option when running docker exec. For example:

   ```bash
    docker exec -it <container_id> /bin/bash
   ```

