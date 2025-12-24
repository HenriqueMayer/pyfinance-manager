### Notes

1. ```docker-compose.yml```:
    - Without the **Docker Compose** tool, managing multi-container Docker applications would be cumbersome. It simplifies the process of defining and running multi-container Docker applications by using a YAML file to configure the application's services, networks, and volumes.
    - Example without Docker Compose:
      ```bash
        docker run -d \
        --name pyfinance_db \
        -p 5432:5432 \
        -e POSTGRES_USER=admin \
        -e POSTGRES_PASSWORD=admin \
        -e POSTGRES_DB=finance_db \
        -v postgres_data:/var/lib/postgresql/data \
        postgres:15-alpine
      ```
      - This command would need to be run manually each time, and managing multiple services would require additional commands and scripts.

2. ```docker compose up -d```:
    - **Parsing the Command**:
        - Docker reads the .yml file and he understands the services defined within it ```db```.
        - State Validation: Docker checks if the container is already running. If it is, it will not recreate it unless there are changes in the configuration.
        - The Compose creates a network for the services to communicate if not already present.
        - Volume Management: Docker ensures that the volume `postgres_data` is created and mounted to the correct path in the container.
        ```yml
        services:
          db:
            image: postgres:15-alpine
            environment:
              POSTGRES_USER: admin
              POSTGRES_PASSWORD: admin
              POSTGRES_DB: finance_db
            ports:
              - "5432:5432"
            volumes:
              - postgres_data:/var/lib/postgresql/data
        ```