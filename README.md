# Sekai AI Platform

A futuristic, customizable AI chat platform featuring Sekai AI, glassmorphism UI, and a foundation for user-created AIs.

## Features

- Neon/cyberpunk glassy UI
- FastAPI backend for authentication, user, AI, and admin management
- React frontend with routing, modern styles, and Sekai branding
- Modular: easily expand with chat, dashboard, and user AI customization

## Getting Started

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Next Steps

- Connect frontend to backend APIs
- Implement real authentication and database
- Add chat, AI customization, and admin controls