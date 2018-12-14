#!/usr/bin/python3

import sys
from mainwindow import *

argCount = len(sys.argv)
mainwindow = MainWindow

if argCount != 2:
    print("Please provide a filename: 'vymthon filename.ext'")
elif argCount == 2:
    filepath = str(sys.argv[1])
    mainwindow = mainwindow(filepath)
