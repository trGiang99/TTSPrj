from aeneas.executetask import ExecuteTask
from aeneas.task import Task


# create Task object
config_string = \
    'task_language=vi|is_text_type=plain|os_task_file_format=json'
task = Task(config_string=config_string)

task.audio_file_path_absolute = 'textData/nhaGiaKim-aeneas-16.mp3'
task.text_file_path_absolute = 'textData/nhaGiaKim-aeneas-16.txt'
task.sync_map_file_path_absolute = 'textData/syncmap16.json'

# process Task
ExecuteTask(task).execute()
# output sync map to file
task.output_sync_map_file()
