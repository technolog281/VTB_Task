FROM acidrain/python-poetry:3.9-slim-1.1.15
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry install
COPY app /app/app
ENV PYTHONPATH=/app
CMD ["poetry", "run", "uvicorn", "--host=0.0.0.0", "app:app"]
