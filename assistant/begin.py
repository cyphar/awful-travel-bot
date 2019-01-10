#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

import re

def on_enter_state(contxt, output=print):
	output("Hello, I'm an _excellent_ travel bot!")
	output("Tell me all about where you've been and I'll recommend a great place for you to go!")

def on_input(data, context, output=print):
	# Are we in a _positive_ state?
	m = re.match(r"^I (?P<mood>(really )?(loved|liked)) (?P<place1>\w+)( and (?P<place2>\w+))?$", data, re.IGNORECASE)
	if m:
		context["mood"] = m.group("mood")
		context["place1"] = m.group("place1")
		context["place2"] = m.group("place2")

		if context["place2"]:
			# Shortcut -- we're all done!
			return "TWO REAL PLACE"
		else:
			# Let's go the long way.
			return "ONE REAL PLACE"

	# Are we in a negative state?
	m = re.match(r"^I (?P<mood>(really )?(hated|disliked)) (?P<place1>\w+)-(?P<place2>\w+)$", data, re.IGNORECASE)
	if m:
		context["mood"] = m.group("mood")
		context["place1"] = m.group("place1")
		context["place2"] = m.group("place2")
		return "FAKE PLACE"

	# No idea.
	if data == "i want burger":
		output("How about no.")
	return "END"
