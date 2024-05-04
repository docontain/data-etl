FROM postgres:15.1

ENV POSTGRES_DB target_db
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password

COPY init.sql /docker-entrypoint-initdb.d/