#!/usr/bin/env python

from secretfy_template import util
from secretfy_template.template import manager

def main():
    """Runs the tool to parse the config. """
    # Read the provided config file which contains the template, secrets file
    # path and desired configuration file extension.
    template_manager = manager.TemplateManager()
    args = util.parse_cli()
    config_list = util.load_config(args.config)
    for config in config_list:
        template_manager.generate(**config)
        if not args.mock:
            template_manager.ignore_secretfy_config_file(args.config)
    if args.mock:
        template_manager.move_mock_files()
