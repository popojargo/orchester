# orchester

This is a python set of tools to easily manage membership of users to your preferred cloud services.

- [orchester](#orchester)
  - [Getting started](#getting-started)
  - [CLI](#cli)
  - [Connectors](#connectors)
    - [Trello](#trello)
    - [Github](#github)
    - [Slack](#slack)
    - [Google Drive](#google-drive)
  - [API](#api)
  - [Contributing](#contributing)
 
## Getting started

Install the package with `pip install orchester`

If you want on using the command line interface, you must define some configurations.

Configuration is done through a `.orchester.json` configuration file. You can see a template here: [.orchester.json](.orchester-doc.json)

The configuration file must be either:

- Path is defined in the **ORCHESTER_CONFIG_PATH** environment variable.
- In the current working directory
- In the user folder (home)

## CLI

Orchester is distributed with a command line tool. Once installed, you can call it with `orchest --help`

The following commands are available:

- `orchest -c CONNECTOR_TYPE check IDENTIFIER`
- `orchest -c CONNECTOR_TYPE add IDENTIFIER`
- `orchest -c CONNECTOR_TYPE rm IDENTIFIER`
- `orchest generate CONNECTOR_TYPE`: Generates the OAuth credentials for connector.


If you want to omit the `CONNECTOR_TYPE` for each command, you can set a default connector in your configuration file:

> "default_connector": "trello"

The connector_type must be **CONNECTOR** name of a valid connector. The connectors are described in the next section.

  
## Connectors

### Trello

**CONNECTOR**: trello

**IDENTIFIER**: Use the trello username

---

1. Get your API token and secret from https://trello.com/app-key
2. Run `/bin/trello_token.py` script to get the credentials
3. Set the OAuth token and OAuth secret in the .env file

---

### Github

**CONNECTOR**: github

**IDENTIFIER**: Use the github username

---

To use the Github service, you need an Personal Token.

Go on Github under `Settings > Developer settings > Personal access tokens`

Then, create a new token and save it in your `.env` file.


---

### Slack

**CONNECTOR**: slack

**IDENTIFIER**: Use the slack email

---

To get started with slack, you first need to get a legacy token and a oauth token.

**Legacy token**

Simply go to the following url and issue a new legacy token: https://api.slack.com/custom-integrations/legacy-tokens

>**Note**: You'll need to be connected to issue a token.

**OAuth token**

Since Slack use Oauth tokens, we have to do some operations.

1. Start the `bin/slack_token.py` server.
2. Go to: `http://localhost:8888/begin_auth`
3. Click on "Add to slack"


**Warnings**

Since we are only using the FREE version, we can't use the api to remove a user.

--- 

### Google Drive

**IDENTIFIER**: Use the google email

**CONNECTOR**: g_drive

---

Before you begin, you'll need a `google_drive_credentials.json` file at the root of this folder.

You can get it by creating credentials in your Google Console API

**Tutorial**: Tutorials coming from: https://developers.google.com/drive/api/v3/quickstart/python

Once you have created your credential file, you can run `bin/gdrive_token.py` to create the `google_drive_token.json`


## API

The API is pretty straight forward.  Each connectors inherit from `orchester.connectors.AbstractBaseConnector`

If you want to use all the connectors at one time, you can use the `orchester.ConnectorManager`

The manager instantiate all the connectors and let you easily interact with the connector one at a time.


Here's an example to use the github connector:
```python
from orchester.connectors import GithubConnector, RequestFailedError

connector = GithubConnector(access_token="my token...",organization_id='myOrg')

try:
    user_exist = connector.is_registered_to_group('popojargo')
    print('User is registered to myOrg')
except RequestFailedError:
    print('The request failed.')


try:
    connector.remove_from_group('popojargo')
    print('User removed to myOrg')

except RequestFailedError:
    print('The request failed.')
    

try:
    user_exist = connector.add_to_group('popojargo')
    print('User added to myOrg')

except RequestFailedError:
    print('The request failed.')
```

## Contributing

For developer documentation, see [README-DEV.md](README-DEV.md)
