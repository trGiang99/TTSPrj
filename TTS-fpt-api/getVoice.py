from env import *
from request_to_FPT_Speech_Synthesize import request_to_FSS
from merge_mp3 import merge_mp3
import subprocess

# Remove BOM character from text file
subprocess.Popen([
    'powershell.exe',
    'removeBOM.ps1'
])


temp = INPUT_DIR.split('/')
temp.reverse()
input_name = temp[0].split('.')[0]      # Output directory


# Read data from text file
file = open(f'textData/{input_name}.txt', 'r', encoding='utf-8')
content = file.read()


# Send request to FPT Speech Synthesize
request_to_FSS(content)


# Merge mp3 file to destination mp3 file
merge_mp3(input_name)
