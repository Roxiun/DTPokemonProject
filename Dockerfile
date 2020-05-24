# Use this to build the container: docker build . -t pokemon-project -f Dockerfile
# Use this to run the container: docker run -d -p 5000:5000 --rm pokemon-project:latest

FROM python:3.6-alpine

RUN mkdir /project
WORKDIR /project
ADD . /project

RUN chmod +x boot.sh

RUN pip install -r requirements.txt

ENV FLASK_APP app.py

EXPOSE 5000
CMD flask run --host=0.0.0.0