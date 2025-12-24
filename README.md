# PyFinance-Manager

Personal finance management application focused on Data Engineering and Artificial Intelligence.
The goal is to replace manual spreadsheets with a robust system capable of generating financial insights through LLMs.

## Technology Stack

- Language: Python 3.12+
- Package Manager: uv
- Database: PostgreSQL 15
- ORM: SQLModel (SQLAlchemy + Pydantic)
- Infrastructure: Docker & Docker Compose

## Infrastructure and Architecture

### The Database (docker-compose.yml)
The data infrastructure is managed via Docker to ensure isolation and reproducibility. The `docker-compose.yml` file defines:

1.  Service `db`: A container running the `postgres:15-alpine` image (lightweight Linux distribution).
2.  Persistence: Uses a Docker Volume (`postgres_data`) to ensure financial data is not lost when the container restarts.
3.  Networking: Exposes port `5432` of the container to `5432` on the host (localhost), allowing Python to connect to the database without running inside Docker.

### Connection Validation
During setup, communication between the local Python environment (host) and the database (container) was validated to ensure that:
- Environment credentials match those defined in the container.
- TCP/IP traffic flows correctly between the OS and Docker.

## How to Run

1. Start the infrastructure:
   ```bash
   docker compose up -d
   ```