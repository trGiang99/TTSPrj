from env import removeBOMfromInputFile, get_list_input
from request_to_FPT_Speech_Synthesize import request_to_FSS
from merge_mp3 import merge_mp3


removeBOMfromInputFile()


inputs = get_list_input()
for item in inputs:   
    # Read data from text file
    file = open(f'textData/{item}.txt', 'r', encoding='utf-8')
    content = file.read()

    # Send request to FPT Speech Synthesize
    request_to_FSS(content)

    # Merge mp3 file to destination mp3 file
    merge_mp3(item)
