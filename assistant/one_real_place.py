#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

def on_enter_state(contxt, output=print):
	output("Sounds lovely! Where else did you go?")

def on_input(data, context, output=print):
	context["place2"] = data
	return "TWO REAL PLACE"
