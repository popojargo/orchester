# orchester

[![PyPI version](https://badge.fury.io/py/orchester.svg)](https://badge.fury.io/py/orchester)![PyPI downloads](https://img.shields.io/pypi/dm/orchester.svg)

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

## Configuration

Configuration is done through a `.orchester.json` configuration file. 
You can see a documented template here: [.orchester-doc.json](.orchester-doc.json)
The values labeled by `[CLI]` are only required for the CLI.

>**Note**: An empty template is available here: [.orchester.json](.orchester-empty.json)


The application will attempt to load from this following order:

- A specific path defined in the **ORCHESTER_CONFIG_PATH** environment variable.
- In the current working directory
- In the user folder (home)

## CLI

Orchester is distributed with a command line tool. Once installed, you can call it with `orchest --help`

The following commands are available:

- `orchest -c CONNECTOR_TYPE check IDENTIFIER`: Check if the user is registered to the organization
- `orchest -c CONNECTOR_TYPE add IDENTIFIER` Add a user to the organization
- `orchest -c CONNECTOR_TYPE rm IDENTIFIER`: Remove a user from the organization
- `orchest generate CONNECTOR_TYPE`: Generates the OAuth credentials for connector.

If you want to omit the `CONNECTOR_TYPE` for each command, you can set a default connector in your configuration file:

> "default_connector": "trello"

The connector_type must be **CONNECTOR** name of a valid connector. The connectors are described in the next section.

  
## Connectors

### Trello

**CONNECTOR**: trello

**IDENTIFIER**: Use the trello username

---

1. Get your API token and secret from https://trello.com/app-key (Look for the Api Key and OAuth secret)
2. Add the Api Key and OAuth secret in the `.orchester.json` configuration file in **api_key** and **api_secret**.
3. Run `orchest generate trello` script to get the credentials
4. Set the OAuth token and OAuth secret in the configuration file in **token** and **token_secret**

---

### Github

**CONNECTOR**: github

**IDENTIFIER**: Use the github username

---

To use the Github service, you need an Personal Token.

Go on Github under `Settings > Developer settings > Personal access tokens`

Then, create a new token and save it in your configuration file at **token**.


---

### Slack

**CONNECTOR**: slack

**IDENTIFIER**: Use the slack email

---

To get started with slack, you first need to get a legacy token and a OAuth token.

**Legacy token**

Simply go to the following url and issue a new legacy token: https://api.slack.com/custom-integrations/legacy-tokens

You can then add the legacy token in **legacy_token**.

>**Note**: You'll need to be connected to issue a token.

**OAuth token**

Before you can actually generate an OAuth token, you'll need to have a Slack application. 

> **How to create an app?**: Go to https://api.slack.com/apps and click on *Create New App* <br />
You must add the following permission scopes: **users:read** and **users:read.email** <br />
You will also need to set the following Redirect URI: http://localhost:8888/finish_auth

You can then store the client id and client secret in **client_id** and **client_secret**

You are now all setup to generate the final OAuth token.

1. Run `orchest generate slack`
2. Go to: `http://localhost:8888/begin_auth`
3. Click on "Add to slack"
4. Click Authorize
5. It should show a OAuth token. Save that in the configuration file at **token** 


>**Warnings**: Free Slack users can't use the api to remove a user.

--- 

### Google Drive

**IDENTIFIER**: Use the google email

**CONNECTOR**: g_drive

---

Before you begin, you'll need a `google_drive_credentials.json` file at the root of this folder.

You can get it by creating credentials in your Google Console API

**Tutorial**: Tutorials coming from: https://developers.google.com/drive/api/v3/quickstart/python

Once you have the `credentials.json` file, you need to define the **credential_path** and **token_path**.

After that, you can run `orchest generate g_drive` to create the `google_drive_token.json`.

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
