# pyinstaller build command:
# pyinstaller.exe --onefile --noconsole --icon=./resources/image_resources/param_sfo.ico start_edit_param_sfo.py
# pyinstaller.exe --onefile --icon=./resources/image_resources/webman.ico ./resources/tools/util_scripts/build_all_scripts.py
# NOTE: '--noconsole' is optional and seems to give a false positive on my AV

import os
import subprocess
from shutil import rmtree

if not os.path.exists('./build'):
	os.makedirs('./build')

script_filename='./ftp_game_list.py'
script_folder_path='../'

icon_path='../../../images/'
icon_name='ftp_game_list.ico'

executable_name='FTP_Game_List'
dist_path='../../../../'
spec_path='./build'

zip_dir_path = './../../../../'
zip_archive_name = 'webman_classics_maker.zip'

app = 'pyinstaller.exe'
args = '--distpath=' + dist_path + ' ' + '--specpath=' + spec_path + ' ' + '--name=' + executable_name + ' ' + '--onefile' + ' ' + '--icon=' + icon_path + icon_name + ' ' + script_folder_path + script_filename

p = subprocess.call(app + ' ' + args)

# clean up the old archive build
if os.path.isfile(zip_dir_path + 'release'):
	os.remove(zip_dir_path + zip_archive_name)
	
# clean up residuals from pyinstaller
rmtree('./build')

print('Succesfully built \"' + executable_name + '.exe\"')
os.system("pause")