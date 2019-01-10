#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

from assistant import STATES

def main():
	# Starting point.
	state, context = "BEGIN", {}

	# Go until we hit our final state.
	while state != "END":
		# Process the current state.
		STATES[state].on_enter_state(context)

		# Get our next bit of text.
		data = input("> ")

		# Parse, figure out the next state and move on.
		state = STATES[state].on_input(data, context)


if __name__ == "__main__":
	main()
