#!usr/bin/env python


"""Manager of template process.

This module generates the template process which parses the template and
secrets file and generates desired configuration file.
"""

from secretfy_template.template import template
from secretfy_template import config
import shutil
import os.path
from os import path


class TemplateManager:

    def __init__(self):
        self._template = template.Template()

    def generate(self, **kwargs):
        template = kwargs.get('template')
        secret = kwargs.get('secret')
        extension = kwargs.get('extension')
        template = config.get_absolute_path(template)
        secret = config.get_absolute_path(secret)
        config_file = self._template.generate(secret, template, extension)
        self._template.exclude_from_git(config_file)

    def ignore_secretfy_config_file(self, config_file):
        self._template.ignore_secretfy_config_file(config_file)

    def move_mock_files(self):
        """Move the mock template, secret and config files to
        /tmp/secretfy-config-creator
        """
        dir = '/tmp/secretfy-config-creator'
        dir_exists = path.exists(dir)
        if not dir_exists:
            os.mkdir(dir)
        self.move_files(dir, "yaml")
        self.move_files(dir, "json")
        self.move_files(dir, "xml")
        baseconfig = config.get_absolute_path('baseconfig.yaml')
        conf = config.get_absolute_path('config.yaml')
        shutil.copyfile(baseconfig, dir+'/baseconfig.yaml')
        shutil.copyfile(conf, dir+'/config.yaml')

    def move_files(self, root, format):
        dir = root + "/" + format
        dir_exists = path.exists(dir)
        if not dir_exists:
            os.mkdir(dir)
        absolute_path = config.get_config_path()
        shutil.copyfile(
            '%s/res/example.%s' % (absolute_path, format),
            dir + '/example.%s' % (format))
        shutil.copyfile(
            '%s/res/secrets.%s' % (absolute_path, format),
            dir + '/secrets.%s' % (format))
        shutil.copyfile(
            '%s/res/example.%s.mustache' % (absolute_path, format),
            dir + '/example.%s.mustache' % (format))
