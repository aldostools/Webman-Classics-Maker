# pyinstaller build command:
# pyinstaller.exe --onefile --noconsole --icon=./resources/image_resources/param_sfo.ico start_edit_param_sfo.py
# pyinstaller.exe --onefile --icon=./resources/image_resources/webman.ico ./resources/tools/util_scripts/build_all_scripts.py
# NOTE: '--noconsole' is optional and seems to give a false positive on my AV

import os
import subprocess
import sys
from shutil import rmtree

import add_application_path
from global_paths import AppPaths
from global_paths import BuildPaths
from global_paths import ImagePaths

if not os.path.exists('build'):
    os.makedirs('build')

script_filename = 'webman-classics-maker.py'
script_folder_path = AppPaths.application_path

icon_path = ImagePaths.misc
icon_name ='webman.ico'

executable_name='webman-classics-maker'
dist_path = AppPaths.application_path
spec_path = 'build'

hidden_imports = '--hidden-import=' + 'configparser' + ' ' + '--hidden-import=' + 'glob' + ' ' + '--hidden-import=' + 'tqdm' + ' ' + '--hidden-import=' + 'pkgcrypt'

app = 'pyinstaller.exe'
args = hidden_imports + ' ' + '--distpath=' + dist_path + ' ' + '--specpath=' + spec_path + ' ' + '--name=' + executable_name + ' ' + '--onefile' + ' ' + '--icon=' + os.path.join(icon_path, icon_name) + ' ' + os.path.join(script_folder_path, script_filename)

p = subprocess.call(app + ' ' + args)


# clean up residuals from pyinstaller
def clean_up(path):
    items = os.listdir(path)
    for item in items:
        if item.endswith(".pyc") or item in ["__pycache__", "build"]:
            rmtree(os.path.join(path, item))


clean_up(AppPaths.util_scripts)
clean_up(AppPaths.wcm_gui)
clean_up(AppPaths.build_scripts)
clean_up(AppPaths.ps3py)

# open builds folder in windows explorer
if 'win' in sys.platform:
    # print('DEBUG opening folder: ' + os.path.join(AppPaths.game_work_dir, '..'))
    try:
        os.startfile(os.path.join(BuildPaths.release))
    except:
        print('ERROR: Could open the pkg build dir from Windows explorer')

print('\n----------------------------------------------------')
print('Succesfully built \"' + executable_name + '.exe\"')
print('----------------------------------------------------\n\n')