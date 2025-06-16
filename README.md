AI Translator News Prototype
This project is a news article platform that translates English articles to Somali using the facebook/nllb-200-distilled-600M model. The backend is built with Django and uses an external Render PostgreSQL database. The frontend uses React + Vite. This guide will help you set up and run the project locally using Docker.
Prerequisites

Docker and Docker Compose installed (Install Docker).
Node.js (optional, for generating package-lock.json locally if needed).
A .env file (provided separately) with DATABASE_URL and SECRET_KEY.

Project Structure

Backend/: Django backend with translation logic and API.
Frontend/: React + Vite frontend.
docker-compose.yml: Defines services for backend and frontend.

Setup Instructions

Clone the Repository
git clone <repository-url>
cd AI_translator


Set Up the .env File

Copy the .env file I sent you to the Backend/ directory:cp /path/to/provided/env/file Backend/.env


The .env file should contain:DATABASE_URL=postgresql://newsdb_zlju_user:<password>@dpg-d17t5kbuibrs738427ig-a.oregon-postgres.render.com/newsdb_zlju
SECRET_KEY=<your-secure-secret-key>


Do not commit .env to Git! Ensure Backend/.env is in .gitignore.


Generate package-lock.json for Frontend

Navigate to the Frontend/ directory and run:cd Frontend
npm install


This creates package-lock.json. If you don’t have Node.js installed, use Docker:docker run --rm -v $(pwd)/Frontend:/app -w /app node:18 npm install


Verify package-lock.json exists:ls Frontend

You should see package.json and package-lock.json.


Build and Start Containers

From the project root (AI_translator/), build and run the Docker containers:docker-compose up --build


This builds and starts:
Backend (Django) on http://localhost:8000
Frontend (React + Vite) on http://localhost:5173




Create a Superuser for Admin Access

Open a new terminal and run:docker-compose exec backend python manage.py createsuperuser


Follow the prompts to create a username, email, and password.


Access the Application

Frontend: Open http://localhost:5173 in your browser.
Backend API: Test with curl http://localhost:8000/api/articles/ or visit in a browser.
Admin Panel: Go to http://localhost:8000/admin/ and log in with the superuser credentials.


Test Translation

Log in to the admin panel (http://localhost:8000/admin/).
Create a new article with English title and content (title_en, content_en).
Save and verify that Somali translations (title_so, content_so) are generated automatically.



Notes

Database: The project uses an external Render PostgreSQL database (configured in .env).
Media Files: Uploaded files (e.g., images) are stored in Backend/media/. Ensure this directory exists:mkdir -p Backend/media


Frontend Development: Edit React code in Frontend/src/. Changes are hot-reloaded.
Backend Development: Edit Django code in Backend/. Run migrations if models change:docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate


Logs: Check for errors with:docker-compose logs backend
docker-compose logs frontend



Troubleshooting

Frontend Build Fails:
Ensure package-lock.json exists in Frontend/.
Run npm install in Frontend/ or use the Docker command above.


Backend Build Slow:
Builds may take time due to large dependencies (torch, transformers). Be patient or check logs:docker-compose logs backend


Clear Docker cache if needed:docker-compose build --no-cache




Database Connection Issues:
Verify DATABASE_URL in Backend/.env matches the provided credentials.
Test connectivity:docker-compose exec backend psql $DATABASE_URL


Check Render’s dashboard for database status.


Translation Errors:
If translations fail, check logs for transformers errors.
Try forcing CPU in Backend/articles/utils.py (edit self.device = "cpu").



For Deployment

This setup is for local development. For production (e.g., Render), contact me for additional steps (e.g., adjusting for Render’s environment, using S3 for media).

