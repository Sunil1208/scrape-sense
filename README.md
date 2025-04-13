# 🕸️ ScrapeSense

**Sense the web. Extract with precision.**  
ScrapeSense is an AI-first web scraping platform that transforms natural language prompts into structured, actionable data using LLMs, Playwright, RabbitMQ, and Redis — built with Django and Celery.

---

## 📛 Badges

![Docker](https://img.shields.io/badge/docker-ready-blue)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Django](https://img.shields.io/badge/django-4.x-success.svg)
![License](https://img.shields.io/github/license/yourusername/scrapesense)
![OpenAI](https://img.shields.io/badge/powered%20by-GPT4-purple.svg)

---

## 🚀 Features

- 🌐 Convert natural language into scrape-ready configurations via GPT
- ⚙️ Queue-powered task execution with RabbitMQ + Celery
- 🧠 LLM response caching (no repeated prompt costs)
- 🕸️ Browser-based scraping with Playwright (headless)
- 📦 Export results in CSV / XLSX format
- 🔐 Multi-tenant role-based auth (User, Admin, Owner)
- 📊 Dashboard with usage stats, errors, and history
- 🔁 Retry failed jobs automatically
- 📣 Email, Slack & Webhook notifications
- 🔐 API tokens, SDK integrations (coming soon)
- 💳 Plan-based usage limits, quotas, and tiering

---

## 🧱 Architecture Overview

```plaintext
┌───────────────┐
│ Frontend UI   │  ← React / Vue (planned)
└──────┬────────┘
       │ HTTP
┌──────▼──────────┐       ┌────────────────┐
│ Django Backend  │──────▶│ LLM (OpenAI)   │
│ (DRF + Services)│       └────────────────┘
│                │
│ ┌────────────┐ │
│ │ Celery     │◀───────┐
│ └────────────┘ │      │
└──────┬──────────┘      │
       ▼                 │
┌────────────┐   ┌────────────────┐
│ RabbitMQ   │   │ Redis (Cache)  │
└────────────┘   └────────────────┘
       │
       ▼
┌─────────────┐
│ Playwright  │ ← Scraper engine
└────┬────────┘
     ▼
┌─────────────┐
│ Exports     │ ← CSV/XLSX stored in S3 or local
└─────────────┘


⚙️ Tech Stack
Layer	Stack
Framework	Django 4.x
Async Tasks	Celery
Queue Broker	RabbitMQ
Cache	Redis
Scraper Engine	Playwright
LLM	OpenAI / Ollama (optional)
File Export	Pandas + CSV/XLSX
Storage	PostgreSQL, S3 / MinIO
Frontend (Planned)	React.js / Vue.js
Auth	JWT + RBAC
Monitoring	Flower, Prometheus (future)
Containerization	Docker + Docker Compose
🧑‍💻 Local Development Setup
Prerequisites
Docker & Docker Compose

OpenAI API key (for GPT)

Python 3.11 (if running without Docker)

🔧 Using Docker
bash
Copy
Edit
git clone https://github.com/yourusername/scrapesense.git
cd scrapesense

cp .env.example .env

# Build and run all services
docker-compose up --build
Services:

web – Django backend

celery – Background task worker

redis – Cache

rabbitmq – Queue broker + UI on http://localhost:15672

db – PostgreSQL database

## 📊 Dashboard & Features Coming Soon
- Web-based scrape creation & monitoring
- Data previews
- Team collaboration
- SDKs for Python / JS
- Plan management & billing (Stripe)
- Custom webhook integrations

## 🧠 Naming Origin
> “ScrapeSense” combines scraping and sensory intelligence — helping you sense, structure, and scale the web’s information automatically.

## 🗺️ Roadmap
- [ ] Multi-tenant setup
- [ ] Celery + RabbitMQ queue integration
- [ ] LLM prompt-to-selector generation
- [ ] Redis caching
- [ ] Dashboard UI (React)
- [ ] API usage stats
- [ ] Proxy management module
- [ ] SDKs (Python + JS)
- [ ] Plan-based rate limiting
- [ ] OAuth & social login

🗺️ Roadmap
 Multi-tenant setup

 Celery + RabbitMQ queue integration

 LLM prompt-to-selector generation

 Redis caching

 Dashboard UI (React)

 API usage stats

 Proxy management module

 SDKs (Python + JS)

 Plan-based rate limiting

 OAuth & social login

🪪 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
We welcome contributions!
Please open issues, submit pull requests, or start a discussion.

Planned:

 CONTRIBUTING.md

 CODE_OF_CONDUCT.md