#!/usr/bin/env python


"""Template plugin to generate final configuration file.

This module defines the :class:`Template` class that read the template and
secret file and generates the final configuration file.
"""


import os
import jinja2
import git
from secretfy_template.secret import manager


class Template:
    """Template configuration generator plugin. """


    def __init__(self):
        """Creates an instance of :class:`Template` plugin. It creates an
        instance of :class:`SecretsManager` required for parsing multiple
        format secrets file
        """
        self._secret_manager = manager.SecretsManager()

    def generate(self, secrets, template, extension):
        """Generates configuration file from given template and secrets.

        Arguments:
            secrets (str): absolute path of secrets file.
            template (str): absolute path of template file.
            extension (str): file format type of configuration file.

        Returns:
            str: absolute path of the generated configuration file.
        """
        template_path = os.path.dirname(template)
        full_file_name = os.path.basename(template)
        filename = full_file_name.split(".")[0]
        config_file = template_path + "/" + filename + "." + extension
        template_file = open(template, 'r')
        file = open(config_file, 'w')
        d = self._secret_manager.get_secret(secrets)
        src = jinja2.Template(template_file.read())
        result = src.render(**d)
        file.write(result)
        file.close()
        return config_file

    def exclude_from_git(self, config_file):
        """Makes sure that the generated configuration file doesn't show in git
        status.

        Arugments:
            config_file (str): absolute path of the genrated configuration
            file.
        """
        git_root_dir = self._get_git_repo_path(config_file)
        config_file = config_file.replace(git_root_dir, "")
        if self._is_file_ignored(config_file):
            return
        git_ignore_file = open('%s/.git/info/exclude'%(git_root_dir), 'a+')
        git_ignore_file.write("{}\n".format(config_file))
        git_ignore_file.close()

    def _is_file_ignored(self, config_file):
        """Add the configuration file to exclude configuration.

        Arugments:
            config_file (str): absolute path of the genrated configuration
            file.
        """
        git_ignore_file = open(".git/info/exclude", 'r')
        for line in git_ignore_file:
            if config_file.strip() == line.strip():
                git_ignore_file.close()
                return True
        git_ignore_file.close()
        return False

    def _get_git_repo_path(self, file_path):
        """ Get git repo root dir path. """

        git_repo = git.Repo(file_path, search_parent_directories=True)
        git_root = git_repo.git.rev_parse("--show-toplevel")
        return git_root
