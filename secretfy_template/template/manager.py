#!usr/bin/env python


"""Manager of template process.

This module generates the template process which parses the template and secrets file and generates desired configuration file.
"""

from secretfy_template.template import template

class TemplateManager:

    def __init__(self):
        self._template = template.Template()

    def generate(self, **kwargs):
        template = kwargs.get('template')
        secret = kwargs.get('secret')
        extension = kwargs.get('extension')
        generatedFile = self._template.generate(secret, template, extension)
        self._template.exclude_from_git(generatedFile)
