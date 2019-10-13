#!/usr/bin/env python

from secretfy_template import util
from secretfy_template.template import manager

def main():
    """Runs the tool to parse the config. """
    #Read the provided config file which contains the template, secrets file path and desired configuration file extension.
    template_manager = manager.TemplateManager()
    template_manager.generate(**util.load_config())
main()
