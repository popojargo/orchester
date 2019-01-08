# orchestrer

This is a python set of tools to easily manage membership of users to your preferred cloud services.


## Trello

**CONNECTOR**: trello

**USERNAME**: Use the trello username

---

1. Get your API token and secret from https://trello.com/app-key
2. Run the trello_token.py script in `/bin`
3. Set the oauth token and oauth secret in the .env file


## Github

**CONNECTOR**: github

**USERNAME**: Use the github username

---

To use the Github service, you need an Personal Token.

Go on Github under `Settings > Developer settings > Personal access tokens`

Then, create a new token and save it in your `.env` file.


---

## Slack

**CONNECTOR**: slack

**USERNAME**: Use the slack email

---

To get started with slack, you first need to get a legacy token and a oauth token.

### Legacy token

Simply go to the following url and issue a new legacy token: https://api.slack.com/custom-integrations/legacy-tokens

>**Note**: You'll need to be connected to issue a token.

### OAuth token

Since Slack use Oauth tokens, we have to do some operations.

1. Start the `bin/slack_token.py` server.
2. Go to: `http://localhost:8888/begin_auth`
3. Click on "Add to slack"


### Warnings

Since we are only using the FREE version, we can't use the api to remove a user.

--- 

## Google Drive setup

**USERNAME**: Use the google email

**CONNECTOR**: g_drive

---

Before you begin, you'll need a `google_drive_credentials.json` file at the root of this folder.

Tutorials coming from: https://developers.google.com/drive/api/v3/quickstart/python

1. Enable API-DRIVE
