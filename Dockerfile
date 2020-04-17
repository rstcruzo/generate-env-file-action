FROM python:3

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY . .

ENTRYPOINT [ "docker-entrypoint.sh" ]