#!/usr/bin/env python


"""Template plugin to generate final configuration file.

This module defines the :class:`Template` class that read the template and
secret file and generates the final configuration file.
"""


import os
import jinja2
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
        templatePath = os.path.dirname(template)
        fullfilename = os.path.basename(template)
        filename = fullfilename.split(".")[0]
        configFile = templatePath + "/" + filename + "." + extension
        templateFile = open(template, 'r')
        file = open(configFile, 'w')
        d = self._secret_manager.get_secret(secrets)
        src = jinja2.Template(templateFile.read())
        result = src.render(**d)
        file.write(result)
        file.close()
        return configFile

    def exclude_from_git(self, config_file):
        """Makes sure that the generated configuration file doesn't show in git
        status.

        Arugments:
            config_file (str): absolute path of the genrated configuration
            file.
        """
        dir_path = os.getcwd()
        config_file = config_file.replace(dir_path, "")
        if self._is_file_ignored(config_file):
            return
        gitignoreFile = open(".git/info/exclude", 'a+')
        gitignoreFile.write("{}\n".format(config_file))
        gitignoreFile.close()

    def _is_file_ignored(self, config_file):
        """Add the configuration file to exclude configuration.

        Arugments:
            config_file (str): absolute path of the genrated configuration
            file.
        """
        gitignoreFile = open(".git/info/exclude", 'r')
        for line in gitignoreFile:
            if config_file.strip() == line.strip():
                gitignoreFile.close()
                return True
        gitignoreFile.close()
        return False
