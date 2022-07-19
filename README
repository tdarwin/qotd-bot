# QOTD-BOT

This is a simple python script that uses the [Conversation Starter API](https://rapidapi.com/nishujain199719-vgIfuFHZxVZ/api/conversation-starter1/) on RapidAPI to send a Question of the Day question to a slack channel of your choosing.

## ENV Variables to define

- SLACK_CHANNEL - The channel you want the message to show up in
- SLACK_URL - The URL for your incoming webhook to Slack
- RAPIDAPI_KEY - The API KEY for accessing subscribed API's in RapidAPI
- RAPIDAPI_HOST - The host for the subscribed API on RapidAPI
- CONVO_STARTER_URL - The URL to the Conversation Starter API on RapidAPI

## Make it Run

Put your files in a Docker compatible envfile (I call mine .env because I'm boring)

```shell
docker build qotd-bot:latest .
docker run --env-file .env question-bot:latest
```

## More notes

I've got this running as a GCP [Cloud Run Job](https://cloud.google.com/run/docs/create-jobs), using the [Cloud Scheduler](https://cloud.google.com/run/docs/execute/jobs-on-schedule) to kick it off on a regular schedule.
