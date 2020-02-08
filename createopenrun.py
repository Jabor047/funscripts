""" usage: py.exe createpyfile.py <filename> creates file name in current dir
           py.exe createpyfile.py <filename> <path> creates filename in path"""

import sys
import os
import subprocess

editor_path = 'C:\\Users\\******\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
python_path = 'C:\\Python3\\python.exe'

if len(sys.argv) == 3 and os.isdir(sys.argv[2]):
    pathplusfile = os.path.join(sys.argv[2], sys.argv[1])
    if os.path.exists(pathplusfile):
        print("please change filename a file with "
              "the same name exists in that directory")
    else:
        pyfile = open(pathplusfile, 'w')
        pyfile.close()
        editor = subprocess.Popen([editor_path, pathplusfile])
        editor.wait()
        if editor.poll() is not None:
            print('running script :) ....')
            pyrun = subprocess.Popen([python_path, pathplusfile])


elif len(sys.argv) == 2:
    currentdir = os.getcwd()
    pathandfile = os.path.join(currentdir, sys.argv[1])
    if os.path.exists(pathandfile):
        print("Please change filename. A file with the same"
              " name exists in the current directory")
    else:
        pyfile = open(pathandfile, 'w')
        pyfile.close()
        editor = subprocess.Popen([editor_path, pathandfile])
        print(editor.poll())
        editor.wait()
        (print(editor.poll()))
        if editor.poll() is not None:
            print('running script :) ....')
            pyrun = subprocess.Popen([python_path, pathandfile])
