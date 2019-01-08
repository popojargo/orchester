# -*- coding: utf-8 -*-
from trello import util
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    util.create_oauth_token()
