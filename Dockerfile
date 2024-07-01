# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.12-slim

# Copy local code to container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies.
RUN pip install -U pip
RUN pip install -U -r requirements.txt

CMD python ${APP_HOME}/question.py