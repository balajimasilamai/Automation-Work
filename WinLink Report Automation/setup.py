from cx_Freeze import setup, Executable
import time
import sys
import win32com.client
import csv
import re
import tkinter
import selenium
import win32api
import shutil
import datetime
import os
import pandas
import numpy
import seaborn
import matplotlib
from threading import Thread
import scipy

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

packages=[
          'shutil',
          'win32api',
          'datetime',          
          'time',
          'win32com.client',
          'tkinter',
          'csv',
          're',
          'selenium',
          'matplotlib',
          'numpy',
          'pandas',
          'threading',
          'pythoncom',
          'sys']

executables = [
    Executable('WinLink_Report_Generation.py', base=base)
]

setup(name='WinLink Report',
      version='0.1',
      description='WinLink Report Automation',
      options={'build_exe':{'packages' :packages, 'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            'C:\\Users\\balaji.ma\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\pypiwin32_system32\\pythoncom36.dll',
            'C:\\Users\\balaji.ma\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\pypiwin32_system32\\pywintypes36.dll',
            'C:\\Users\\balaji.ma\\AppData\\Local\Programs\\Python\\Python36-32\\Lib\\site-packages\\win32\\pythoncom36.dll',
            'C:\\Users\\balaji.ma\\AppData\\Local\Programs\\Python\\Python36-32\\Lib\\site-packages\\win32\\pywintypes36.dll',
         ]

        }
        },
      executables=executables
      )
