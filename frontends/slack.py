#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

import flask

from frontends import app
from assistant import STATES

# Starting states.
state, context = "BEGIN", {}

@app.route("/bot/slack", methods=["GET", "POST"])
def slack_bot():
	# So that the state is the same between requests. This is less than ideal,
	# and there is a persistence talk to help remove this need.
	global state, context

	# Just exit.
	if state == "END":
		return "That's all folks!"

	# For collecting output for returning.
	outputs = []
	output = lambda line: outputs.append(line)

	# Process the current state.
	STATES[state].on_enter_state(context, output=output)

	# Get our next bit of text.
	data = flask.request.values.get("text")
	if not data:
		data = ""

	# Parse, figure out the next state and move on.
	state = STATES[state].on_input(data, context, output=output)

	# Just combine them all.
	return str.join("\n", outputs)
