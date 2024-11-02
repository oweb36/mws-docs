#!/bin/sh

find . -name "*.md" -type f -print0 -exec basename {} \;