#!usr/bin/env python


"""Config util for heimdall.

This class is mainly for config utils like getting the absolute path of the
installed directory.

This is mainly for getting to support --mock implementation too
"""

import os
import os.path as path

import git

_absolute_path = os.path.dirname(os.path.abspath(__file__))


def get_config_path():
    """Get the absolute path of the installed directory.

    """
    return _absolute_path


def get_absolute_path(file_path):
    """Get the absolute path of the file provide. There are multiple scenarios.

        1. It checks whether the provided config is valid or not.
        2. In case if the config file provided is not an absolute path or if
        the absolute path is not correct then there are chances that the user
        is looking for mock files and hence it would try to get the installed
        directory and return the absolute path of file.
        3. If the first 2 conditions are not met then the path isn't correct
        and null values is returned.
    """
    if path.exists(file_path):
        return file_path
    else:
        mock_path = _absolute_path + "/" + file_path
        if path.exists(mock_path):
            return mock_path
    return None


def get_git_repo_path(file_path):
    """ Get git repo root dir path. """

    git_repo = git.Repo(file_path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")

    # special case for /tmp since the path received is /private/tmp
    if git_root.startswith('/private'):
        git_root = git_root.replace('/private', '')
    return git_root
