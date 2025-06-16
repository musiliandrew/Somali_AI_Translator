I’ve prepared a further refined and polished version of the .md file for your AI Translator News Prototype, incorporating best practices for Markdown documentation. This version improves clarity, adds a table of contents, and ensures a professional, user-friendly structure. If you meant a different .md file or have specific changes in mind, please clarify, and I’ll tailor the response accordingly.
markdown
# AI Translator News Prototype

The AI Translator News Prototype is a platform for publishing and translating news articles from English to Somali using the `facebook/nllb-200-distilled-600M` model. The backend is built with Django, connected to an external Render PostgreSQL database, while the frontend uses React with Vite. This guide explains how to set up and run the project locally using Docker.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up the `.env` File](#2-set-up-the-env-file)
  - [3. Generate `package-lock.json` for Frontend](#3-generate-package-lockjson-for-frontend)
  - [4. Build and Start Containers](#4-build-and-start-containers)
  - [5. Create a Superuser](#5-create-a-superuser)
  - [6. Access the Application](#6-access-the-application)
  - [7. Test Translation](#7-test-translation)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
  - [Frontend Build Fails](#frontend-build-fails)
  - [Backend Build Slow](#backend-build-slow)
  - [Database Connection Issues](#database-connection-issues)
  - [Translation Errors](#translation-errors)
- [Deployment](#deployment)

## Prerequisites

Before starting, ensure you have:

- **Docker and Docker Compose**: [Install Docker](https://docs.docker.com/get-docker/).
- **Node.js**: Optional, for local `package-lock.json` generation.
- **.env File**: Provided separately, containing `DATABASE_URL` and `SECRET_KEY`.

## Project Structure

- **`Backend/`**: Django backend with translation logic and API endpoints.
- **`Frontend/`**: React + Vite frontend for the user interface.
- **`docker-compose.yml`**: Configuration for backend and frontend services.

## Setup Instructions

### 1. Clone the Repository

Clone the project and navigate to the directory:

```bash
git clone <repository-url>
cd AI_translator
2. Set Up the .env File

Copy the provided .env file to the Backend/ directory:
bash
cp /path/to/provided/env/file Backend/.env

The .env file should include:
text
DATABASE_URL=postgresql://newsdb_zlju_user:<password>@dpg-d17t5kbuibrs738427ig-a.oregon-postgres.render.com/newsdb_zlju
SECRET_KEY=<your-secure-secret-key>

    Warning: Never commit the .env file to Git. Confirm Backend/.env is in .gitignore.

3. Generate package-lock.json for Frontend

Navigate to the Frontend/ directory and install dependencies:
bash
cd Frontend
npm install

This creates package-lock.json. If Node.js is unavailable, use Docker:
bash
docker run --rm -v $(pwd)/Frontend:/app -w /app node:18 npm install

Verify the files:
bash
ls Frontend

You should see package.json and package-lock.json.
4. Build and Start Containers

From the project root (AI_translator/), build and launch the Docker containers:
bash
docker-compose up --build

This starts:

    Backend (Django): http://localhost:8000
    Frontend (React + Vite): http://localhost:5173

5. Create a Superuser

Open a new terminal and create a superuser for the Django admin panel:
bash
docker-compose exec backend python manage.py createsuperuser

Follow the prompts to set a username, email, and password.
6. Access the Application

    Frontend: Visit http://localhost:5173 in your browser.
    Backend API: Test with curl http://localhost:8000/api/articles/ or open in a browser.
    Admin Panel: Access http://localhost:8000/admin/ and log in with superuser credentials.

7. Test Translation

    Log in to the admin panel (http://localhost:8000/admin/).
    Create an article with English title and content (title_en, content_en).
    Save and confirm Somali translations (title_so, content_so) are generated.

Development Notes

    Database: Uses an external Render PostgreSQL database, configured in .env.

    Media Files: Stored in Backend/media/. Create the directory if needed:
    bash

mkdir -p Backend/media

Frontend Development: Edit code in Frontend/src/. Changes hot-reload automatically.

Backend Development: Modify Django code in Backend/. Apply model changes with:
bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate

Logs: Monitor logs for debugging:
bash

    docker-compose logs backend
    docker-compose logs frontend

Troubleshooting
Frontend Build Fails

    Confirm package-lock.json exists in Frontend/.
    Run npm install in Frontend/ or use the Docker command above.

Backend Build Slow

    Large dependencies (torch, transformers) may slow builds. Check logs:
    bash

docker-compose logs backend

Rebuild without cache if necessary:
bash

    docker-compose build --no-cache

Database Connection Issues

    Verify DATABASE_URL in Backend/.env matches provided credentials.

    Test connection:
    bash

    docker-compose exec backend psql $DATABASE_URL

    Check Render’s dashboard for database status.

Translation Errors

    Inspect logs for transformers issues.
    Force CPU usage in Backend/articles/utils.py by setting self.device = "cpu".

Deployment

This guide covers local development. For production deployment (e.g., on Render), contact the project maintainer for guidance on Render-specific configurations, such as environment settings or S3 for media storage.