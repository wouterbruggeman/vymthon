#!/usr/bin/python3

import sys
from buffer import *
from editorwindow import *

argCount = len(sys.argv)
editorwindow = None
buffer = None

if argCount != 2:
    print("Please provide a filename: 'vymthon filename.ext'")
elif argCount == 2:
    filepath = str(sys.argv[1])
    editorwindow = EditorWindow(filepath)
