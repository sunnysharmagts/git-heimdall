#!/usr/bin/env python

from heimdall import util
from heimdall.template import manager
from heimdall.codescan import manager as codescan
import sys

def main():
    """Runs the tool to parse the config. """
    # Read the provided config file which contains the template, secrets file
    # path and desired configuration file extension.
    template_manager = manager.TemplateManager()
    codescan_manager = codescan.CodescanManager()
    args = util.parse_cli()
    if args.init:
        codescan_manager.init()
        return None
    if args.codescan is not None:
        codescan_manager.scan(sys.argv[2:])
        return
    if args.extension is not None or args.repo is not None or args.secret is not None:
        if args.repo is None:
            print("--repo path required")
            return None
        elif args.extension is None:
            print("--extension required")
            return None
        elif args.secret is None:
            print("--secret required")
            return None
        elif args.secret is None:
            print("--secret required")
            return None
        template_manager.get_all_template_files(args.repo, args.extension, args.secret)
        return None
    config_list = util.load_config(args.config)
    for config in config_list:
        template_manager.generate(**config)
        if not args.mock:
            template_manager.ignore_secretfy_config_file(args.config)
    if args.mock:
        template_manager.move_mock_files()
    return None
