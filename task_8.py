"""
Task8.

8 lines: Command line arguments, exception handling
"""

import sys

"""
This program adds up integers

that have been passed as arguments
in the command line
"""

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
except ValueError:
    print('Please supply integer arguments')
