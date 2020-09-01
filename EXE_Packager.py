# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:03:04 2020

@author: 10653181
"""
import os
from pyshortcuts import make_shortcut


file_abs_path = input(r'please Enter the absolute path of the file... Ex: C:\Users\ABC\Desktop\projects\myapp.py')
def call_external_cmd(f_name):
    os.system(f'pyinstaller {f_name}')
    return

if os.path.exists(file_abs_path) == True:
    print('all cool')
    file_name = file_abs_path.split('\\')[-1]
    print('Processing your files..')
    path_exe = call_external_cmd(file_name)
    a = file_abs_path.split('\\')[0:-1]
    a.append('dist')
    exe_name=file_name.split('.')[0]
    a.append(exe_name)
    a.append(file_name.split('.')[0]+ '.exe')
    d='\\'.join(a)
    print('Your Exe file is at location : ',d)
    
    
    make_shortcut(file_abs_path, name=exe_name)
    print('Shortcut for the your application is created on Desktop')
    
else:
    print('Unable to track the location')

