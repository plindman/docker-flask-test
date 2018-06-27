FROM python:3.6-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt
FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app
# ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:5000 --workers=4"
CMD ["gunicorn", "app:app"]
