#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from unicodecsv import reader
from tabulate import tabulate
from sys import argv

if len(argv) > 1:
    input_file = argv[1]
else:
    print "csv2latex need input file as argument"

output_file=input_file.rsplit('.')[0] + ".tex"
input=open(input_file)
output=open(output_file, 'w')

table=reader(input,encoding='utf-8-sig')

#output.write(tabulate(table,tablefmt='latex'))
print tabulate(table,tablefmt='latex')
