FROM python:3.10-alpine as builder

WORKDIR /usr/src/password

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY . .

COPY ./req.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/password/wheels -r req.txt

FROM python:3.10-alpine

RUN mkdir -p /home/password

RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/password
ENV APP_HOME=/home/password/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add libpq
COPY --from=builder /usr/src/password/wheels /wheels
COPY --from=builder /usr/src/password/req.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

COPY . $APP_HOME

USER root

ENTRYPOINT ["/home/password/web/entrypoint.sh"]