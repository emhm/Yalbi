# Written using Python 2.7
# Not guaranteed to work with any other version of Python

# This script requires the HJSON package
# You can install it with a quick and easy `pip install hjson`

from os import path
import re
import sys

try:
    import hjson
except ImportError:
    print 'No HJSON package!'
    print 'Run `pip install hjson` on a terminal or something'
    raw_input('(Press enter to continue) ')
    sys.exit(1)

scriptname = path.basename(sys.argv[0])

files = '''\
roots_template.md
'''

def format_roots(source):
    return '[TODO]\n'

def format_modifiers(source):
    return '[TODO]\n'

for filename in files.splitlines():
    with open(filename, 'r') as f:
        output = ''
        outfile = None
        for line in f:
            match = re.match(r'~~([^\s]*)(\s+(.*))?\n', line)
            if match is None:
                output += line
            elif match.group(1) == '':
                pass
            elif match.group(1) == 'OUTFILE':
                outfile = match.group(3)
            elif match.group(1) == 'AUTOGEN_WARNING':
                output += '_This file was automatically generated by `{0}`. Do not make changes to this file directly; instead modify {1}._\n'.format(scriptname, match.group(3))
            elif match.group(1) == 'ROOTSLIST':
                output += format_roots(match.group(3))
            elif match.group(1) == 'MODIFIERSLIST':
                output += format_modifiers(match.group(3))
        if outfile is None:
            print 'WARNING: No OUTFILE for {0}!'.format(filename)
        else:
            with open(outfile, 'w') as f:
                f.write(output)