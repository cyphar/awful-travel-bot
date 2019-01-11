#!/usr/bin/env python3
# awful-travel-bot: A really awful travel bot.
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Rights waived via CC0 <https://creativecommons.org/publicdomain/zero/1.0/>.

from . import begin

# BEGIN -> "I liked <place1> and <place2>."
#       -> "Have you tried <place1>-<place2>?"
from . import one_real_place
from . import two_real_place

# BEGIN -> "I disliked <fake-place>."
#       -> "Don't go to <fake> or <place>!"
from . import fake_place

# STATES is a dictionary that maps each state string to one of your state files
# (each of which has an on_input() and on_enter_state() function).
#
#  * on_enter_state(context, output=print) is usually when most processing of
#      the input we just got happens -- this might involve doing some API calls
#      to figure out what is going on in context[place] or similar.
#      on_enter_state really shouldn't modify context.
#
#  * next_state = on_input(data, context, output=print) parses and figures out
#      what the next_state will be, possibly giving some output. next_state is
#      just the same string in STATES.

STATES = {
	"BEGIN": begin,
	"END":   None,

	"FAKE PLACE":     fake_place,
	"ONE REAL PLACE": one_real_place,
	"TWO REAL PLACE": two_real_place,
}
