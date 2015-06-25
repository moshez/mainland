# Copyright (c) Moshe Zadka
# See LICENSE for details.

if __name__ != '__main__':
    raise ImportError('module cannot be imported')

import sys
from mainland import main

main(
    root='mainland',
    marker='MAINLAND_MAIN_OK',
    argv=sys.argv,
)
