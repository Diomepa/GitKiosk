FROM python:3.9-slim-buster as base
ENV PYTHONUNBUFFERED 1
ENV WORK_DIR /app
WORKDIR ${WORK_DIR}
EXPOSE 8000

# install our app requirements
ADD requirements/requirements.txt requirements/requirements.txt
RUN pip install -r requirements/requirements.txt && \
    rm -rf ~/.cache/pip /tmp/pip-build-root

FROM base as bound-dev
ADD requirements/extra-requirements.txt requirements/extra-requirements.txt
RUN pip install -r requirements/requirements.txt && \
    rm -rf ~/.cache/pip /tmp/pip-build-root


FROM base
COPY . .
CMD bash -c "./scripts/run.sh"

