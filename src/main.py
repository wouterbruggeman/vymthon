#!/usr/bin/python3
import sys
from application import Application

#Variables
filepath = ".tmp"
argCount = len(sys.argv)
app = Application()

#Check for parameters
if argCount == 2:
    filepath = str(sys.argv[1])
  
#Open the file if set
app.openFile(filepath)

#Loop the program
while app.isRunning():
    app.loop()
