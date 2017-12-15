# MIT License
#
# Copyright (c) 2017 Tom Melo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# pylint: disable=C0103,C0301,W1202,W0212

"""
The shift module.

This is small cli tool that performs alphanumeric char shifting.
"""

import argparse
import sys
from formatter import CustomFormatter
from alphanumeric import Alphanumeric

parser = argparse.ArgumentParser(prog='shift', usage='shift alpha <options>', formatter_class=CustomFormatter)
parser.add_argument("alpha", nargs="+", help="the alphanumeric string")
parser.add_argument("-p", "--positions", metavar="", help="the number of positions to shift", type=int)
parser.add_argument("-r", "--range", nargs="+", metavar="", help="a range of numbers separated by space")
parser.add_argument("--backwards", action="store_true", help="performs a backward shift")
parser.add_argument("--ignore-numbers", action="store_true", help="ignores every char that is a digit")
parser.add_argument("--ignore-letters", action="store_true", help="ignores every char that is a letter")
parser.add_argument("--version", action="version", version="shift v1.0.0")

parser.set_defaults(positions=1)
parser.set_defaults(range=None)

def is_piped_input():
    """
    Checks the piped input.

    This function checks if this script
    is being executed with a piped input.

    E.g.: echo abcde | python shift.py

    Returns
    -------
    bool
        True if the is a piped input, False otherwise.
    """
    return not sys.stdin.isatty()

def is_piped_output():
    """
    Checks the piped output.

    This function checks if this script
    is being executed with a piped output.
    E.g.: python shift.py abce -p 2 > result.json

    Returns
    -------
    bool
        True if the is a piped output, False otherwise.
    """
    return not sys.stdout.isatty()

def main(args):
    """Executes an alphanumeric string shift"""

    nrange = None
    if args.range:
        nrange = map(int, args.range)

    alphanumeric = Alphanumeric(nrange)
    if args.backwards:
        alpha_func = alphanumeric.backward_alphanumeric
    else:
        alpha_func = alphanumeric.forward_alphanumeric

    result = alpha_func(
        ''.join(args.alpha),
        args.positions,
        ignore_numbers=args.ignore_numbers,
        ignore_letters=args.ignore_letters)

    sys.stdout.write(result)
    if not is_piped_output():
        sys.stdout.write("\n")

if __name__ == "__main__":
    try:
        if is_piped_input():
            alpha = sys.stdin.read().strip()
            cli_args = argparse.Namespace(
                alpha=alpha,
                positions=1,
                range=None,
                backwards=False,
                ignore_numbers=False,
                ignore_letters=False)
        else:
            cli_args = parser.parse_args()

        main(cli_args)
    except KeyboardInterrupt:
        sys.exit()
