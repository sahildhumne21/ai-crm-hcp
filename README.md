# ai-crm-hcp
AI-First CRM HCP Interaction Module using FastAPI, React, LangGraph and Groq LLM

# AI-First CRM – HCP Interaction Module

## Overview

This project implements an **AI-First Customer Relationship Management (CRM) module** for logging and managing interactions with **Healthcare Professionals (HCPs)**.

Field representatives can log interactions with doctors either through a **structured form** or a **conversational AI assistant**.

The system uses **LangGraph** and **Groq LLM** to analyze interactions and assist in summarizing and managing HCP engagement.

---

## Features

### Log HCP Interaction
Sales representatives can log interaction details including:

- HCP Name
- Interaction Type
- Topics Discussed
- Outcome
- Follow-up Actions

### AI Assistant
Users can describe the interaction in natural language and the system processes it using an **LLM**.

Example:

```
Met Dr Sharma and discussed diabetes drug efficacy.
Provided sample pack and planned follow-up meeting.
```

### LangGraph AI Agent
The application uses a **LangGraph agent** to manage CRM workflows and route tasks to the appropriate tools.

### CRM Tools

| Tool | Purpose |
|-----|------|
| log_interaction | Save interaction details |
| edit_interaction | Modify existing interaction |
| get_history | Retrieve previous HCP interactions |
| summarize_interaction | Generate AI summary |
| suggest_followup | Recommend next actions |

### Database Storage
All interaction data is stored in a **SQLite database**.

---

## System Architecture

```
React Frontend
      ↓
FastAPI Backend
      ↓
LangGraph Agent
      ↓
CRM Tools
      ↓
Groq LLM
      ↓
SQLite Database
```

---

## Tech Stack

### Frontend
- React
- Axios
- CSS

### Backend
- Python
- FastAPI
- LangGraph

### AI Model
- Groq LLM
- Model: `llama-3.3-70b-versatile`

### Database
- SQLite

---

## Project Structure

```
AI-CRM-HCP
│
├── backend
│   ├── agents
│   │   └── langgraph_agent.py
│   │
│   ├── tools
│   │   ├── log_interaction.py
│   │   ├── edit_interaction.py
│   │   ├── get_history.py
│   │   ├── summarize_interaction.py
│   │   └── suggest_followup.py
│   │
│   ├── database.py
│   ├── models.py
│   ├── main.py
│   ├── crm.db
│   └── .env
│
└── frontend
    ├── public
    ├── src
    ├── package.json
    └── package-lock.json
```

---

## Installation & Setup

### Clone the Repository

```
git clone <your-repository-url>
cd AI-CRM-HCP
```

---

## Backend Setup

Navigate to backend:

```
cd backend
```

Create virtual environment:

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install fastapi uvicorn groq python-dotenv
```

Run backend server:

```
python -m uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

Open another terminal:

```
cd frontend
```

Install dependencies:

```
npm install
```

Run React app:

```
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## Example Usage

1. Open the application:

```
http://localhost:3000
```

2. Enter interaction text:

```
Met Dr Sharma and discussed diabetes drug efficacy.
Provided sample pack and scheduled follow-up meeting.
```

3. Click **Log Interaction**

4. The AI agent processes the interaction and logs it.

---

## AI Workflow

1. User enters interaction
2. Frontend sends request to FastAPI backend
3. LangGraph agent processes request
4. Agent calls Groq LLM
5. AI response is generated
6. Interaction is stored in database
7. Result returned to UI

---

## Future Improvements

- Authentication system
- HCP profile management
- Analytics dashboard
- Voice-to-text interaction logging
- CRM integrations

---

## Author

**Sahil Dhumne**  
B.Tech Final Year Student  
Aspiring AI Engineer

---

## Assignment Context

This project was developed as part of a **technical assignment to design an AI-First CRM HCP module using LangGraph and LLMs**.

The project demonstrates:

- AI-assisted interaction logging
- Agent-based architecture
<<<<<<< HEAD
- LLM integration in CRM workflows
=======
- LLM integration in CRM workflows
>>>>>>> d53ecfe33524411e0d2661b4a6a27ab564abf64f
