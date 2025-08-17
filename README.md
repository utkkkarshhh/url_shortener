# URL Shortener

A full-stack URL shortening service built with a Python (FastAPI) backend, a React frontend, and orchestrated with Docker Compose. This project allows users to shorten long URLs into concise, shareable links.

## Features

* **URL Shortening:** Convert long URLs into short, unique codes.
* **Redirection:** Redirect short URLs to their original long URLs.
* **User-Specific URLs:** (Assumed based on `get_user_urls_manager.py`) Potentially allows users to manage their shortened URLs.
* **Scalable Architecture:** Utilizes Docker for containerization and DynamoDB for efficient data storage.

## Technologies Used

**Backend:**

* Python 3
* FastAPI (for building the API)
* Boto3 (for AWS DynamoDB interaction)

**Frontend:**

* React (JavaScript library for UI)
* Vite (fast build tool for frontend)

**Database:**

* AWS DynamoDB (NoSQL database, running locally via Docker for development)

**Infrastructure & Orchestration:**

* Docker
* Docker Compose
* Nginx (as a reverse proxy)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to get the URL Shortener up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/utkkkarshhh/url_shortener.git
cd url_shortener
```

### 2. Environment Variables

Both the backend and frontend services require environment variables.

* **Backend (`url_shortner_service`):**
  Navigate to the `url_shortner_service` directory and create a `.env` file by copying the example:

  ```bash
  cd url_shortner_service
  cp .env.example .env
  # Open .env and configure your variables (e.g., DynamoDB endpoint if not local)
  cd .. # Go back to the project root
  ```
* **Frontend (`web`):**
  Navigate to the `web` directory and create a `.env` file by copying the example:

  ```bash
  cd web
  cp .env.example .env
  # Open .env and configure your variables (e.g., API base URL)
  cd .. # Go back to the project root
  ```

### 3. Run with Docker Compose

From the root directory of the project, run the following command to build and start all services:

```bash
docker compose up --build -d
```

* `docker compose up`: Starts the services defined in `docker-compose.yml`.
* `--build`: Builds the Docker images for your services (backend and frontend).
* `-d`: Runs the containers in detached mode (in the background).

### 4. Access the Application

Once all services are up and running (this might take a few moments for the first build), you can access the application:

* **Frontend:** Open your web browser and go to `http://localhost` (or the port Nginx is configured to listen on).
* **Backend API:** The API will typically be accessible via Nginx, e.g., `http://localhost/api/v1/...`

### 5. Stopping the Application

To stop and remove the running containers, networks, and volumes created by `docker compose up`, run:

```bash
docker compose down
```

## Project Structure

* `url_shortner_service/`: Contains the Python FastAPI backend application.
* `web/`: Contains the React frontend application.
* `nginx.conf`: Nginx configuration for routing requests to the backend and serving the frontend.
* `docker-compose.yml`: Defines the multi-container Docker application, including the backend, frontend, Nginx, and DynamoDB (if configured as a service).moDB data.
* `Makefile`: Quick commands for building the dockerised app.
