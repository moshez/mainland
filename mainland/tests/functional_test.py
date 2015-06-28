# Copyright (c) Moshe Zadka
# See LICENSE for details.

import argparse

MAINLAND_MAIN_OK = True

PARSER = argparse.ArgumentParser()

def main(argv):
    res = PARSER.parse_args(argv[1:])    
