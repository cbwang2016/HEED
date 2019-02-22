from cx_Freeze import setup, Executable
import os
import shutil

os.environ['TCL_LIBRARY']=r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY']=r'C:\Program Files\Python36\tcl\tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['lxml','idna.idnadata'], excludes = ['sklearn'])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.pyw', base=base)
]

setup(name='HEED',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)

shutil.copyfile('error.png','build/exe.win-amd64-3.6/error.png')
shutil.copyfile('README.html','build/exe.win-amd64-3.6/README.html')
#'''
os.remove('build/exe.win-amd64-3.6/lib/_hashlib.pyd')
shutil.rmtree('build/exe.win-amd64-3.6/tcl/tzdata')
shutil.rmtree('build/exe.win-amd64-3.6/tcl/msgs')
shutil.rmtree('build/exe.win-amd64-3.6/tcl/encoding')
shutil.rmtree('build/exe.win-amd64-3.6/tk/demos')
shutil.rmtree('build/exe.win-amd64-3.6/tk/images')
shutil.rmtree('build/exe.win-amd64-3.6/tk/msgs')
#'''