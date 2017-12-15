FROM python:3.6-alpine

RUN adduser -D flaskkrkapp

WORKDIR /home/flask_app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY flask_app.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP flask_app.py

RUN chown -R flaskkrkapp:flaskkrkapp ./
USER flaskkrkapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]