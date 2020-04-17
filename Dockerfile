FROM python:3

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY . .
RUN ls

ENTRYPOINT [ "docker-entrypoint.sh" ]