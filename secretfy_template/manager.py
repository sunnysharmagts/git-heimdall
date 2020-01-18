#!/usr/bin/env python

from secretfy_template import util
from secretfy_template.template import manager


def main():
    """Runs the tool to parse the config. """
    # Read the provided config file which contains the template, secrets file
    # path and desired configuration file extension.
    template_manager = manager.TemplateManager()
    args = util.parse_cli()
    if args.extension is not None or args.repo is not None or args.secret is not None:
        if args.repo is None:
            print("--repo path required")
            return
        elif args.extension is None:
            print("--extension required")
            return
        elif args.secret is None:
            print("--secret required")
            return
        elif args.secret is None:
            print("--secret required")
            return
        template_manager.get_all_template_files(args.repo, args.extension, args.secret)
        return
    config_list = util.load_config(args.config)
    for config in config_list:
        template_manager.generate(**config)
        if not args.mock:
            template_manager.ignore_secretfy_config_file(args.config)
    if args.mock:
        template_manager.move_mock_files()
