from aeneas.executetask import ExecuteTask
from aeneas.task import Task
from env import get_list_input

import os


config_string = \
        'task_language=vi|is_text_type=plain|os_task_file_format=json'
task = Task(config_string=config_string)

inputs = get_list_input()
for item in inputs:
    task.audio_file_path_absolute = f'textData/{item}.mp3'
    task.text_file_path_absolute = f'textData/{item}.txt'
    task.sync_map_file_path_absolute = f'textData/syncmap-{item}.json'

    # process Task
    ExecuteTask(task).execute()
    # output sync map to file
    task.output_sync_map_file()
