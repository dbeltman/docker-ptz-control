FROM alpine/git AS cloner
RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/dbeltman/flask-onvif-zeep

FROM python:3.7-alpine
RUN apk add libxml2-dev libxslt-dev gcc musl-dev
WORKDIR /app
COPY --from=cloner /app/flask-onvif-zeep/requirements.txt  .

RUN pip install -r requirements.txt
COPY --from=cloner /app/flask-onvif-zeep/ .


ENTRYPOINT ["python"]
CMD ["main-flask.py"]