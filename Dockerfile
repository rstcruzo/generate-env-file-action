FROM python:3

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY generate-env-file.py .

ENTRYPOINT [ "docker-entrypoint.sh" ]