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
        templates = kwargs.get('templates')
        secret = kwargs.get('secret')
        secret = config.get_absolute_path(secret)
        for template in templates:
            file = template.get('file')
            extension = template.get('extension')
            file = config.get_absolute_path(file)
            config_file = self._template.generate(secret, file, extension)
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
        conf = config.get_absolute_path('baseconfig1.yaml')
        shutil.copyfile(baseconfig, dir+'/baseconfig.yaml')
        shutil.copyfile(conf, dir+'/baseconfig1.yaml')

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

    def get_all_template_files(self, repo, extension, secret):
        my_dict = dict()
        my_dict['secret'] = secret[0]
        templates = []
        if repo is not None:
            for dirpath, dirnames, filenames in \
                    os.walk(repo[0]):
                for filename in [
                        f for f in filenames if f.endswith(extension[0])]:
                    file_name = os.path.join(dirpath, filename)
                    file_extension = os.path.basename(file_name).split('.')
                    template_dict = dict()
                    template_dict['file'] = file_name
                    template_dict['extension'] = file_extension[1]
                    templates.append(template_dict)
            my_dict['templates'] = templates
            self.generate(**my_dict)
            return my_dict
