FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y cron
COPY crontab /etc/cron.d/etl_cron
RUN chmod 0644 /etc/cron.d/etl_cron
RUN crontab /etc/cron.d/etl_cron

CMD ["cron", "-f"]