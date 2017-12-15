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
The alphanumeric module.

This module contains the Alphanumeric class.
The Alphanumeric class is a helper class that performs digit and letter shifting.
"""

class Alphanumeric(object):
    """
    The Alphanumeric class.

    This is a helper class that performs digit and letter shifting.
    """

    ALPHABET_LENGTH = 26

    def __init__(self, nrange=None):
        """
        The class constructor.

        The constructor initializes with a default value
        the following attributes:

            * current_letter = 'z'
            * current_number = 0

        A range of numbers(nrange parameter) can be specified
        to perform a cyclic iterator when shifting numbers.

        Parameters
        -------
        nrange: list
            The number range.
        """
        self.current_letter = 'z'
        self.current_number = 0
        self.nrange = nrange

    def forward_letter(self, letter, positions):
        """
        Forwards N positions of the given letter.

        Eg.:
            letter    = 'a'
            positions = 2

            result = 'c'

        Note: This function will keep a state of the last letter shifted.
              This will have effect when calling the funcions
              next_letter() and previous_letter().
              Eg.:
                  forward_letter('a', 1) // result is 'b'
                  previous_letter()      // result is 'a'
                  next_letter()          // result is 'c'

        Parameters
        -------
        letter: str
            The alphabet letter.
        positions: int
            The number of positions to forward.

        Returns
        -------
        result: str
            The forwarded letter.
        """

        if letter.islower():
            unicode_point = ord('a')
        else:
            unicode_point = ord('A')

        start = ord(letter) - unicode_point
        offset = ((start + positions) % self.ALPHABET_LENGTH) + unicode_point
        self.current_letter = chr(offset)
        return self.current_letter

    def backward_letter(self, letter, positions):
        """
        Backwards N positions of the given letter.

        Eg.:
            letter    = 'a'
            positions = 1

            result = 'z'

        Note: This function will keep a state of the last letter backwarded.
              This will have effect when calling the funcions
              next_letter() and previous_letter().
              Eg.:
                  backward_letter('a', 1) // result is 'z'
                  previous_letter()       // result is 'y'
                  next_letter()           // result is 'a'

        Parameters
        -------
        letter: str
            The alphabet letter.
        positions: int
            The number of positions to backward.

        Returns
        -------
        result: str
            The backwarded letter.
        """

        if letter.islower():
            unicode_point = ord('a')
        else:
            unicode_point = ord('A')

        start = ord(letter) - unicode_point
        offset = ((start - positions) % self.ALPHABET_LENGTH) + unicode_point
        self.current_letter = chr(offset)
        return self.current_letter

    def next_letter(self):
        """
        Forwards 1 position of the current letter.

        Returns
        -------
        result: str
            The forwarded letter.
        """

        return self.forward_letter(self.current_letter, 1)

    def previous_letter(self):
        """
        Backwards 1 position of the current letter.

        Returns
        -------
        result: str
            The backwarded letter.
        """

        return self.backward_letter(self.current_letter, 1)

    def forward_number(self, number, positions):
        """
        Forwards N positions of the given number.

        Eg.:
            number    = 1
            positions = 2

            result = 3

        If a range of numbers has been defined in the class instance
        a cyclic iterator will be performed.
        Eg.:
            nrange    = [1, 2, 3, 4, 5]
            number    = 1
            positions = 7

            result = 3

        Note: This function will keep a state of the last number shifted.
              This will have effect when calling the funcions
              next_number() and previous_number().
              Eg.:
                  forward_number(1, 1) // result is 2
                  previous_number()    // result is 1
                  next_number()        // result is 3

        Parameters
        -------
        number: int
            The number.
        positions: int
            The number of positions to forward.

        Returns
        -------
        result: int
            The forwarded number.
        """

        if not self.nrange:
            self.current_number = number + positions
            return self.current_number

        index = self.nrange.index(number)
        start = index + positions
        offset = (start % len(self.nrange))
        self.current_number = self.nrange[offset]
        return self.current_number

    def backward_number(self, number, positions):
        """
        Backwards N positions of the given number.

        Eg.:
            number    = 1
            positions = 2

            result = -1

        If a range of numbers has been defined in the class instance
        a cyclic iterator will be performed.
        Eg.:
            nrange    = [1, 2, 3, 4, 5]
            number    = 1
            positions = 7

            result = 4

        Note: This function will keep a state of the last number backwarded.
              This will have effect when calling the funcions
              next_number() and previous_number().
              Eg.:
                  backward_number(1, 1) // result is 0
                  previous_number()     // result is -1
                  next_number()         // result is 1

        Parameters
        -------
        number: int
            The number.
        positions: int
            The number of positions to backward.

        Returns
        -------
        result: int
            The backwarded number.
        """

        if not self.nrange:
            return number - positions

        index = self.nrange.index(number)
        start = index - positions
        offset = (start % len(self.nrange))
        self.current_number = self.nrange[offset]
        return self.current_number

    def next_number(self):
        """
        Forwards 1 position of the current number.

        Returns
        -------
        result: int
            The forwarded number.
        """

        return self.forward_number(self.current_number, 1)

    def previous_number(self):
        """
        Backwards 1 position of the current number.

        Returns
        -------
        result: int
            The backwarded number.
        """

        return self.backward_number(self.current_number, 1)

    def forward_alphanumeric(self, alpha, positions, ignore_numbers=False, ignore_letters=False):
        """
        Forwards N positions of the given alphanumeric string.

        Eg.:
            alpha     = 'abc123'
            positions = 1

            result = 'bcd234'

        All non alphanumeric characters are ignored.

        Note: This function will keep a state of the last number and letter found
              on the given alphanumeric phrase. This will have effect when calling
              the funcions next_number(), previous_number(), next_letter() and previous_letter().
              Eg.:
                  forward_alphanumeric('abc123', 1) // result is 'bcd234'
                  next_letter()                     // result is 'e'
                  next_number()                     // result is 5

        Parameters
        -------
        alpha: str
            The alphanumeric string.
        positions: int
            The number of positions to forward.
        ignore_numbers: bool
            Ignores all digits on the given alphanumeric string
        ignore_letters: bool
            Ignores all the alphabet letters on the given alphanumeric string

        Returns
        -------
        result: int
            The forwarded alphanumeric string.
        """

        result = ""
        for char in alpha:
            if char.isdigit() and not ignore_numbers:
                char = str(self.forward_number(int(char), positions))

            if char.isalpha() and not ignore_letters:
                char = self.forward_letter(char, positions)

            result += char

        return result

    def backward_alphanumeric(self, alpha, positions, ignore_numbers=False, ignore_letters=False):
        """
        Backwards N positions of the given alphanumeric string.

        Eg.:
            alpha     = 'abc123'
            positions = 1

            result = 'zab012'

        All non alphanumeric characters are ignored.

        Note: This function will keep a state of the last number and letter found
              on the given alphanumeric phrase. This will have effect when calling
              the funcions next_number(), previous_number(), next_letter() and previous_letter().
              Eg.:
                  backward_alphanumeric('abc123', 1) // result is 'zab012'
                  next_letter()                      // result is 'c'
                  next_number()                      // result is 3

        Parameters
        -------
        alpha: str
            The alphanumeric string.
        positions: int
            The number of positions to backward.
        ignore_numbers: bool
            Ignores all digits on the given alphanumeric string
        ignore_letters: bool
            Ignores all the alphabet letters on the given alphanumeric string

        Returns
        -------
        result: int
            The backwarded alphanumeric string.
        """

        result = ""
        for char in alpha:
            if char.isdigit() and not ignore_numbers:
                char = str(self.backward_number(int(char), positions))

            if char.isalpha() and not ignore_letters:
                char = self.backward_letter(char, positions)

            result += char

        return result
