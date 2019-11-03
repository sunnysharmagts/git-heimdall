#!usr/bin/env python


"""Manager of template process.

This module generates the template process which parses the template and
secrets file and generates desired configuration file.
"""

from secretfy_template.template import template
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
        config_file = self._template.generate(secret, template, extension)
        self._template.exclude_from_git(config_file)

    def ignore_secretfy_config_file(self, config_file):
        self._template.ignore_secretfy_config_file(config_file)    

    def move_mock_files(self):
        """Move the mock template, secret and config files to /tmp/secretfy-config-creator
        """
        dir = '/tmp/secretfy-config-creator'
        dir_exists = path.exists(dir)
        if not dir_exists:
            os.mkdir(dir)
        self.move_files(dir, "yaml")
        self.move_files(dir, "json")
        self.move_files(dir, "xml")
        shutil.copyfile('baseconfig.yaml', dir+'/baseconfig.yaml')
        shutil.copyfile('config.yaml', dir+'/config.yaml')

    def move_files(self, root, format):
        dir = root + "/" + format
        dir_exists = path.exists(dir)
        if not dir_exists:
            os.mkdir(dir)
        shutil.copyfile('secretfy_template/res/example.%s'%(format), dir+'/example.%s' %(format))
        shutil.copyfile('secretfy_template/res/secrets.%s'%(format), dir+'/secrets.%s'%(format))
        shutil.copyfile('secretfy_template/res/example.%s.mustache'%(format), dir+'/example.%s.mustache'%(format))
