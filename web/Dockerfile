FROM python:3.6-alpine as base
FROM base as builder
RUN ash -c 'mkdir -p /web/app'
RUN ash -c 'mkdir -p /install/lib/python3.6/site-packages'
ENV PYTHONPATH /install/lib/python3.6/site-packages
COPY setup.py /web/setup.py
WORKDIR /web
RUN pip install --install-option="--prefix=/install" -e .
#COPY requirements.txt /install/requirements.txt
#RUN pip install --install-option="--prefix=/install" -r requirements.txt
FROM base
COPY --from=builder /install /usr/local
COPY --from=builder /web/app.egg-info/ /web/app.egg-info/
# app files linked via volumes
WORKDIR /web
# CMD ["flask", "run"]
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:5000 --workers=4 --reload"
CMD ["gunicorn", "app:app"]
