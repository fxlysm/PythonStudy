import distutils
# import py2exe
# distutils.core.setup(windows=['wxTest.py'])

#coding=utf-8
from distutils.core import setup
import py2exe
setup(console=["wxTest.py"])
setup(Windows=["wxTest.py"],options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}})
