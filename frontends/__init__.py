#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

import flask
app = flask.Flask(__name__)

import frontends.slack
