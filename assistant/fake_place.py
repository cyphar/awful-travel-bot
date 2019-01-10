#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

def on_enter_state(context, output=print):
	output(f"Oh boy, if you {context['mood']} that, then definitely don't think of going to {context['place1']} or {context['place2']}!")
	output("You promise?")

def on_input(data, context, output=print):
	if "yes" in data.lower():
		output("Phew. Place is really scary.")
	if "no" in data.lower():
		output("I really hope you reconsider...")
	return "END"
