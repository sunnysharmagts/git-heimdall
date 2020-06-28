#!/usr/bin/env python3

import os
import subprocess
import sys


def scan():
    _pwd = sys.argv[1]
    _files = sys.argv[2:]
    _file_list = ' '.join(_files)
    printDescription(_pwd, _file_list)
    p = subprocess.run(["heimdall", "-scan", _pwd, _file_list],
                       capture_output=True)
    _byte_output = p.stdout
    _final_output = _byte_output.decode()
    _exit_code = 0
    _final_output = _final_output.strip()
    if len(_final_output) > 0:
        _exit_code = 1
        # Ask user whether he wants to still resume with the commit
        color_print('\x1b[91m', 'Your files has some sensitive data.', '\x1b[0m\n')
        print(_final_output)
        _continue_with_commit = ''
        sys.stdin = open('/dev/tty')
        while len(_continue_with_commit) == 0:
            _continue_with_commit = input('Do you want to continue with the commit ?(y/n): ')
        _continue_with_commit = _continue_with_commit.lower()
        if(_continue_with_commit == 'y' or _continue_with_commit == 'yes'):
            _exit_code = 0
        elif(_continue_with_commit == 'n' or _continue_with_commit == 'no'):
            _exit_code = 1
            revert_commit(_pwd)
    else:
        print('\x1b[92mCongratulations~!!!. There is no sensitive data in your files.\x1b[0m\n')
    sys.exit(_exit_code)


def color_print(start_tag, text, end_tag):
    print(start_tag+text+end_tag)


def revert_commit(root_dir):
    subprocess.run(["cd", root_dir], capture_output=True)
    subprocess.run(["git", "reset", "*"], capture_output=True)


def printDescription(root, file_name_list):
    print('#' * 100)
    print('\n')
    print('[INFO] Initiating the scanning process...')
    print('\n')
    print('#' * 100)
    print('\n')
    print('[INFO] Scanning the following files:\n')
    file_name_list = file_name_list.split()
    for file in file_name_list:
        print('[INFO] ', '.' * 20, os.path.join(root, file))
    print('\n')
    print('[INFO] This will take few seconds...')


if __name__ == "__main__":
    scan()
