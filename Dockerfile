FROM python:3.10


WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install psycopg2-binary

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./alembic /backend/alembic
COPY ./alembic.ini /backend
COPY ./src /backend/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]