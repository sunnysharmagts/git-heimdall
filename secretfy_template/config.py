import os
import os.path as path

_absolute_path = os.path.dirname(os.path.abspath(__file__))

def get_config_path():
    return _absolute_path

def get_absolute_path(file_path):
    if path.exists(file_path):
        return file_path
    else:
        mock_path = _absolute_path+ "/" + file_path
        if path.exists(mock_path):
            return mock_path
    return None
