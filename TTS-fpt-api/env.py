import subprocess
import os

API_KEYS_DIR = 'keys.txt'       # File contains API keys
INPUT_DIR = 'textData'    # File contains input text data

"""
Xác định các giọng đọc. Voice có các giá trị là:
    leminh (giọng nam miền bắc)
    male (giọng nam miền bắc)
    female (giọng nữ miền bắc)
    hatieumai (giọng nữ miền nam)
    ngoclam (giọng nữ Huế)
"""
VOICE = "leminh"
SPEED = "0"     # Tốc độ đọc
PROSODY = "0"   # Ngữ điệu 1 on. 0 off


def removeBOMfromInputFile():
    """
    Remove BOM character from every text file
    """
    powerShellPath = r'C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe'
    p = subprocess.Popen(
        [powerShellPath, 
        '-ExecutionPolicy', 'Unrestricted', 
        r'.\removeBOM.ps1'], 
    )
    p.communicate()


def get_file_name(ipath):
    """Get file name from given path
    
    Arguments:
        ipath {str}
    """
    file_name = ipath.split('.')[0]      
    
    return file_name


def get_list_input():
    """
    Get a list of input text file
    """
    list_input = []

    for item in os.listdir(INPUT_DIR):
        if item.endswith('.txt'):
            file_name = get_file_name(item)
            list_input.append(file_name)
    return list_input