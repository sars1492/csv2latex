#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# csv2latex.py -- Converts CSV data to LaTeX table.
#
# Copyright (C) 2017  Juraj Szász <juraj.szasz3@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""Converts CSV data to LaTeX table.

usage: csv2latex.py [-h] [-v] [-o FILE] FILE

Converts FILE (in CSV format) into LaTeX table and send the output to
STDOUT. Optionally, if -o argument is specified, the output is written into the
file instead.

positional arguments:
  FILE           input file

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -o FILE        write output to FILE

"""

from __future__ import unicode_literals
import argparse
import unicodecsv
import sys
from tabulate import tabulate

__version__ = "0.1"


# Set default encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    """Run initial code when this module is executed as a script.

    1. Parse command line arguments using argparse.ArgumentParser object.
    2. Load input CSV file using unicodecsv.reader()
    3. Convert CSV data into LaTeX table using tabulate.tabulate()
    4. Write output into the output file or print output to STDOUT.

    """
    description = "Converts FILE (in CSV format) into LaTeX table and send " + \
                  "the output to STDOUT.  Optionally, if -o argument is " + \
                  "specified, the output is written into the file instead."
    arg_parser = argparse.ArgumentParser(description=description)
    arg_parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    arg_parser.add_argument("-o", metavar="FILE", dest='output_file', type=argparse.FileType('w'),
                            help="write output to FILE")
    arg_parser.add_argument("input_file", metavar="FILE", type=argparse.FileType('r'),
                            help="input file")
    args = arg_parser.parse_args()

    csv_reader = unicodecsv.reader(args.input_file, encoding='utf-8-sig')
    output = tabulate(csv_reader, tablefmt='latex')

    if args.output_file:
        args.output_file.write(output)
    else:
        print output


if __name__ == "__main__":
    # This code is executed only when scientometry-data-proc is being run
    # directly as a script.  Since local variables are allocated much faster
    # than global variables, it is a good practice to encapsulate whole initial
    # code into the main() function.
    main()
