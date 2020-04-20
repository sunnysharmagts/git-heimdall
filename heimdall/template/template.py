#!/usr/bin/env python


"""Template plugin to generate final configuration file.

This module defines the :class:`Template` class that read the template and
secret file and generates the final configuration file.
"""

import logging
import os
import os.path

import jinja2

from heimdall import config
from heimdall.secret import manager

_log = logging.getLogger(__name__)


class Template:
    """Template configuration generator plugin. """

    def __init__(self):
        """Creates an instance of :class:`Template` plugin. It creates an
        instance of :class:`SecretsManager` required for parsing multiple
        format secrets file
        """
        self._secret_manager = manager.SecretsManager()
        self._git_root_dir = None

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
        self.exclude_from_git(secrets)
        return config_file

    def exclude_from_git(self, config_file):
        """Makes sure that the generated configuration file doesn't show in git
        status.

        Arguments:
            config_file (str): absolute path of the genrated configuration
            file.
        """
        try:
            self._git_root_dir = config.get_git_repo_path(config_file)
        except git.exc.InvalidGitRepositoryError:
            return
        config_file = config_file.replace(self._git_root_dir, "")
        if self._is_file_ignored(config_file, self._git_root_dir):
            return
        git_ignore_file = open(
            '%s/.git/info/exclude' % (self._git_root_dir),
            'a+')
        git_ignore_file.write("{}\n".format(config_file))
        git_ignore_file.close()

    def ignore_secretfy_config_file(self, config_file):
        """This method ignores the config file which contains template, secrets
        and extension metadata.

        Arguments:
            config (str): absolute path of the secretfy config file of yaml
            format
        """
        for config in config_file:
            if not os.path.exists(config):
                continue
            file_name = None
            config = config.rsplit('/', 1)
            config = config[len(config)-1]
            if self._git_root_dir is not None:
                for dirpath, dirnames, filenames in \
                        os.walk(self._git_root_dir):
                    for filename in [
                            f for f in filenames if f.endswith(config)]:
                        file_name = os.path.join(dirpath, filename)
                        line = open(file_name, 'r').readline()
                        if line == 'heimdall':
                            break
                self.exclude_from_git(file_name)

    def _is_file_ignored(self, config_file, project_git_dir):
        """Add the configuration file to exclude configuration.

        Arugments:
            config_file (str): absolute path of the genrated configuration
            file.
        """
        git_ignore_file = open(
            '%s/.git/info/exclude' % (project_git_dir),
            'r')
        for line in git_ignore_file:
            if config_file.strip() == line.strip():
                git_ignore_file.close()
                return True
        git_ignore_file.close()
        return False
