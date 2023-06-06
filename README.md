# Life Script backend

This is a project i've started because i've always been interested in making fullstack applications that me and other people can use. I originally started this project after getting inspired by applications like Notion and Obsidian.

TODO Explain visions and the development process for this project!

## Tech Stack

**Framework:** FastAPI

**Database:** PostgreSQL

**Database Management:** Pgadmin4

**Container Managment:** Docker

**Things you need installed to run this project:**

- Python 3.10^
- Docker

## Run Locally

Clone the project

```bash
  git clone https://github.com/OriginalDCAM/lifescript-backend
```

Go to the project directory

```bash
  cd lifescript-backend
```

Create a virtual environment

```bash
  virtualenv venv
```

Activate virtual environment

```bash
  source venv/bin/activate
```

Install dependencies locally

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  docker compose up -d
```

Run the migrations

```bash
  alembic upgrade head
```
