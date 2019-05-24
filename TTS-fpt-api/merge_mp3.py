import subprocess
import os


def merge_mp3(input_name):
    """Merge mp3 file to destination mp3 file

    Arguments:
        input_name {str} -- Path to where all mp3 file are stored to merge
    """
    with open('download/create_list.bat', 'w') as f:
        f.write("(for %%i in (*.mp3) do @echo file '%%i') > list.txt")
    os.chdir('download')

    subprocess.Popen("create_list.bat")
    os.chdir('..')

    # Merge file
    # Output file: {outputfỉ}.txt
    subprocess.run(
        'ffmpeg -f concat -safe 0 -i'
        f' download/list.txt -c copy textData/{input_name}.mp3'
    )

    for item in os.listdir('download'):
        if item.endswith(".mp3"):
            os.remove(os.path.join('download/', item))
