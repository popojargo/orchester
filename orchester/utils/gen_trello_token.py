# -*- coding: utf-8 -*-
from trello import util
from orchester.ConfigHelper import get_config_data, pick


def generate():
    config = get_config_data()
    cfg = pick(config, 'connectors.trello')
    api_key = pick(cfg, 'api_key')
    api_secret = pick(cfg, 'api_secret')

    util.create_oauth_token(key=api_key, secret=api_secret)


if __name__ == '__main__':
    generate()
