#!/usr/bin/env python3

import argparse, sys, glob, os, datetime
import xml.etree.ElementTree as ET

# Setup argument parser
parser = argparse.ArgumentParser(
                    description="Compiles markdown files into XML."
                        )
parser.add_argument("-o", "--output", 
                    dest="output",
                    help="Where to output the generated XML.",
                    type=str,
                    default="a.xml")
parser.add_argument("-r", "--recursive",
                    dest="recursive",
                    help="Recursively traverse the directory for XML?",
                    type=bool,
                    default=True)
parser.add_argument("-i", "--include-hidden",
                    dest="includehidden",
                    help="Include hidden?",
                    action="store_true")
parser.add_argument("where",
                    help="Which directory to traverse?",
                    type=str)
args = parser.parse_args(sys.argv[1:])

where = args.where # Where is the directory to search for
recursive = args.recursive # Recursively search?
output = args.output # Output XML file
includehidden = args.includehidden # Include hidden files?

# Construct the Tree with sone default tags
root = ET.Element("mdcompxml")
ET.SubElement(root, "meta", when=str(datetime.date.today().strftime("%B %d, %Y %I:%M:%S %p")))

# Find all files
for file in glob.glob("**/*.md", root_dir=where, recursive=recursive, include_hidden=includehidden):
    bfile = os.path.basename(file)
    print(bfile)

tree = ET.ElementTree(root)
tree.write(output, encoding="UTF-8", xml_declaration=True)