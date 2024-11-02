#!/usr/bin/env python3

import argparse, sys, glob
import xml.etree.ElementTree as ET

# Setup argument parser
parser = argparse.ArgumentParser(
                    description="Compiles markdown files into XML."
                        )
parser.add_argument("-o", "--output", 
                    dest="output",
                    help="Where to output the generated XML.")
parser.add_argument("-r", "--recursive",
                    dest="recursive",
                    help="Recursively traverse the directory for XML?")
args = parser.parse_args(sys.argv[1:])