#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

def on_enter_state(context, output=print):
	new_place = f"{context['place1']}-{context['place2']}?"

	output(f"Wow! Have you checked out {new_place} yet?")
	output(f"If you {context['mood']} the last place, this'd be even greater!")

def on_input(data, context, output=print):
	if "yes" in data.lower():
		output("That's too bad. Guess you've seen quite a bit in your travels.")
	if "no" in data.lower():
		output("I'd totally recommend it (if it existed)!")
	return "END"
