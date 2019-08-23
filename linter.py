#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Bruno JJE
# Copyright (c) 2015 Bruno JJE
#
# License: MIT
#

"""This module exports the Xvlog plugin class."""

from SublimeLinter.lint import Linter


class Xvlog(Linter):

    """Provides an interface to xvlog (from Xilinx Vivado Simulator)."""

    name = 'xvlog'
    cmd = 'xvlog @'
    defaults = {
        'selector': 'source.v',
    }

    # Here is a sample xvlog error output:
    # ----8<------------
    # ERROR: [VRFC 10-91] td_logic is not declared [/home/project/src/filter.v:35]
    # ----8<------------

    regex = (
        r"^(?P<error>ERROR: )(?P<message>\[.*\].*)"
        r"\[(?P<path>.*):(?P<line>[0-9]+)\]"
    )

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method to prefix the error message with the
        linter name.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if match:
            message = '[xvlog] ' + message

        return match, line, col, error, warning, message, near
