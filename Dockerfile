FROM python:3.7-slim-buster as production

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"

EXPOSE 80
WORKDIR /app

COPY Pipfile* /app/
RUN pip install pipenv && \
    pipenv install --system --deploy
ADD . /app/
RUN chmod +x scripts/* && \
    pybabel compile -d locales -D bot

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["run-webhook"]
