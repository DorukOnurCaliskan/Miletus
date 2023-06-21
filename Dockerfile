FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /miletus_backend
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
CMD flask db init ; \
flask db stamp head && \
flask db migrate && \
flask db upgrade && \
gunicorn --workers 2 --timeout 120 -b 0.0.0.0:5000 --reload miletus:app
