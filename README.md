# csv2latex

A simple yet ingenious script that converts CSV data into LaTeX table and sends
the output to STDOUT.  Optionally the output can be written into the file
instead.


## Installation

The `csv2latex.py` script requires `unicodecsv` and `tabulate` Python packages
to run.  The script itself is usually placed into the working directory,
although it could be useful to place it e.g. into `~/bin` directory and add
`~/bin` to `PATH`.

Following subsections describe how to install the dependency packages.


### Fedora

    $ sudo dnf install -y python-unicodecsv python-tabulate


### CentOS/RHEL

    $ sudo pip install unicodecsv tabulate


### Ubuntu/Debian

    $ sudo apt-get install python-unicodecsv python-tabulate


### Other Linux distro, Apple macOS, Other UNIX-like OS

    $ sudo pip install pyyaml unicodecsv tabulate


### MS Windows

    > python -m pip install -U pip setuptools
    > python -m pip install unicodecsv tabulate


## Synopsis

```
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
```


## Usage examples

1. Convert input CSV data into LaTeX table and print output to `STDIN`

        $ ./csv2latex.py data.csv

2. Convert input CSV data into LaTeX table and redirect output into file:

        $ ./csv2latex.py data.csv > table.tex

3. You can also specify output file via argument:

        $ ./csv2latex.py -o table.tex data.csv

4. Convert input CSV data into LaTeX table and add output to file:

        $ ./csv2latex.py data.csv >> tables.tex

5. Making `csv2latex.py` globally accessible:

        $ cp csv2latex.py ~/bin
        $ export PATH=$PATH:~/bin
        $ cd ~/data
        $ ls
        data.csv
        $ csv2latex.py -o table.tex data.csv


## License

csv2latex.py -- Converts CSV data to LaTeX table.

Copyright (C) 2017  Juraj Szasz (<juraj.szasz3@gmail.com>)

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hopet hat it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
