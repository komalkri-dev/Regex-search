#!/usr/bin/env python
"""regex_script.py: This script searches for lines matching regular expression -r (--regex) in file/s -f (--files)."""
__author__ = "Komal Kumari"
__email__ = "komalkri7044@gmail.com"

import argparse
import os
import sys
import re
from optional_argument import OptionalArgument
from termcolor import colored

def argument_parser():
    parser = argparse.ArgumentParser(description="This script searches for lines matching regular \
                                                    expression -r (--regex) in file/s -f (--files)\
                                                    with some optional arguments", add_help=True)
                                                    
    parser.add_argument('-f','--files', nargs='*', type=argparse.FileType('r'),
                        help='name of the file(s) to search a string matches with -r regular expression')
    parser.add_argument('-r','--regex', help='the regular expressio to match.')

    exclusive_grp = parser.add_mutually_exclusive_group()
    exclusive_grp.add_argument('-u', '--underscore', action='store_true', help='prints "^" under the matching text.')
    exclusive_grp.add_argument('-c', '--color', action='store_true', help='highlights the matching text.')
    exclusive_grp.add_argument('-m', '--machine', action='store_true', help='generates machine readable output in format: file_name:no_line:start_pos:matched_text')

    return parser

if __name__ == "__main__":
    args = argument_parser().parse_args()
    if not (args.files and args.regex):
        print(colored("-f and -r arguments are mandatory to input file and regular expression", "white", "on_red"))
        print(argument_parser().parse_args(['-h']))
    for file in args.files:
        for i, line in enumerate(file):
            matches = re.finditer(args.regex, line)
            if matches:
                for match in matches:
                    option = OptionalArgument(file.name, line[:-1], i+1)
                    if args.underscore:
                        option.underscore_option(match.start(), match.end())
                    elif args.color:
                        option.color_option(match.group())
                    elif args.machine:
                        option.machine_option(match.start(),match.group())
                    else:
                        option.printline()
                  

