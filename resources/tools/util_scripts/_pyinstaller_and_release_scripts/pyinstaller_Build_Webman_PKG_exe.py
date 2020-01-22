# pyinstaller build command:
# pyinstaller.exe --onefile --noconsole --icon=./resources/image_resources/param_sfo.ico start_edit_param_sfo.py
# pyinstaller.exe --onefile --icon=./resources/image_resources/webman.ico ./resources/tools/util_scripts/build_all_scripts.py
# NOTE: '--noconsole' is optional and seems to give a false positive on my AV

import os, subprocess, sys
from shutil import rmtree
import application_path

from global_paths import App as AppPaths
from global_paths import Build as BuildPaths
from global_paths import Image as ImagePaths

if not os.path.exists('build'):
	os.makedirs('build')

script_filename='build_pkg.py'
script_folder_path=BuildPaths.pyinstaller

icon_path=ImagePaths.misc
icon_name='webman.ico'

executable_name='Build_Webman_PKG'
dist_path=AppPaths.resources
spec_path='build'

app = 'pyinstaller.exe'
args = '--distpath=' + dist_path + ' ' + '--specpath=' + spec_path + ' ' + '--name=' + executable_name + ' ' + '--onefile' + ' ' + '--icon=' + os.path.join(icon_path, icon_name) + ' ' + os.path.join(script_folder_path, script_filename)

p = subprocess.call(app + ' ' + args)


# clean up residuals from pyinstaller
if os.path.isdir('build'):
	rmtree('build')
if os.path.isdir('__pycache__'):
	rmtree('__pycache__')
	
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'pyc' in str(file):
            os.remove(file)

print('\n----------------------------------------------------')
print('Succesfully built \"' + executable_name + '.exe\"')
print('----------------------------------------------------\n\n')