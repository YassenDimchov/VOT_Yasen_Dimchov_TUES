FROM python:3.13.0

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

COPY app/ /app/

RUN pip install -r requirements.txt

COPY init_db.sql /app/init_db.sql

RUN python /app/init_db.py

EXPOSE 5000

CMD ["python", "/app/app.py"]