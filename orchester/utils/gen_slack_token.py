from flask import Flask, request, jsonify
from slackclient import SlackClient
from orchester.ConfigHelper import get_config_data, pick


def generate():
    config = get_config_data()
    cfg = pick(config, 'connectors.slack')

    client_id = pick(cfg, 'client_id')
    client_secret = pick(cfg, 'secret')
    oauth_scope = "users:read,users:read.email"
    print("Go to http://localhost:8888/begin_auth")

    app = Flask(__name__)

    @app.route("/begin_auth", methods=["GET"])
    def pre_install():
        return '''
          <a href="https://slack.com/oauth/authorize?scope={0}&client_id={1}">
              Add to Slack
          </a>
      '''.format(oauth_scope, client_id)

    @app.route("/finish_auth", methods=["GET", "POST"])
    def post_install():
        # Retrieve the auth code from the request params
        auth_code = request.args['code']

        # An empty string is a valid token for this request
        sc = SlackClient("")

        # Request the auth tokens from Slack
        auth_response = sc.api_call(
            "oauth.access",
            client_id=client_id,
            client_secret=client_secret,
            code=auth_code
        )
        return jsonify(auth_response['access_token'])
        # print('Bot token {}'.format(auth_response['bot']['bot_access_token']))

    app.run(host='0.0.0.0', port=8888)


if __name__ == '__main__':
    generate()
