# 📚 Academic Notes Organizer

A web-based platform for students to organize their courses, lecture notes, and study materials — all in one clean, searchable archive. 🎓

---

## ✨ What is this?

Managing scattered notes and files across a semester is painful. This project solves that by giving each student a personal academic archive: create courses, attach notes and files to them, and browse everything through a **file-explorer-style tree UI**. 🗂️

---

## 🚀 Features

- 🔐 **User Accounts** — registration & login powered by Django's built-in authentication system
- 📖 **Course Management** — create, edit, and delete your courses
- 📝 **Notes with Markdown** — write rich notes using a built-in Markdown editor
- 📎 **File Uploads** — attach PDFs, images, and Word documents to your notes (Django Media Files)
- 🔍 **Full-Text Search** — instantly search across note titles and content
- 🌲 **Tree Navigation** — browse courses and notes like a file explorer
- 📊 **User Dashboard** — personal overview with advanced filtering options
- 🐘 **PostgreSQL** — production-grade database instead of SQLite
- 🐳 **Dockerized** — the whole stack runs with a single `docker compose up`

---

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| Backend | Django (MVT) 🐍 |
| Frontend | HTML / CSS 🎨 |
| Database | PostgreSQL 🐘 |
| Container | Docker & Docker Compose 🐳 |
| Editor | Markdown ✍️ |

---

## ⚡ Quick Start
```bash
git clone https://github.com/AmirrezaGoleij/academic-notes-organizer.git
cd academic-notes-organizer
docker compose up --build

Then open 👉 [http://localhost:8000](http://localhost:8000)

---

## 🗃️ Data Model


User 👤 ──< Course 📖 ──< Note 📝 ──< Attachment 📎

- **User** — owns courses
- **Course** — title, description, owner
- **Note** — title, description, markdown content, timestamps
- **Attachment** — uploaded files linked to notes

---

## 🧪 Tests

bash
docker compose exec web python manage.py test

---

## 🏗️ Architecture Notes

The structure is built around `Course` and `Note`, designed to be easily extensible toward a **notes marketplace** in the future (public profiles, global search, ratings & reviews). 🔮

---

## 🎓 Academic Context

This project was developed as part of the **Advanced Programming** course at the University of Guilan 🏛️, during Semester 2, under the supervision of Prof. Amirhossein Tabatabaei.

---

Made by [Amirreza Goleij]
(https://github.com/AmirrezaGoleij)
