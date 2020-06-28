#!/usr/bin/env python

import sys

from heimdall import util
from heimdall.codescan import manager as codescan
from heimdall.template import manager


def main():
    """Runs the tool to parse the config. """
    # Read the provided config file which contains the template, secrets file
    # path and desired configuration file extension.
    _template_manager = manager.TemplateManager()
    _codescan_manager = codescan.CodescanManager()
    args = util.parse_cli()
    if args.init:
        _codescan_manager.init()

    elif args.codescan is not None:
        print(_codescan_manager.scan(sys.argv[2:]))

    elif args.register is not None:
        _codescan_manager.register(sys.argv[2:])

    elif args.un_register is not None:
        _codescan_manager.unregister(sys.argv[2:])

    elif check_all_template_args(args, _template_manager):
        return

    else:
        config_list = util.load_config(args.config)
        for config in config_list:
            if not config:
                print('Cannot find the config file. Please provide correct \
                       path of the config.')
                continue
            _template_manager.generate(**config)
            if not args.mock:
                _template_manager.ignore_secretfy_config_file(args.config)
        if args.mock:
            _template_manager.move_mock_files()


def check_all_template_args(args, template_manager):
    if not hasattr(args, 'extension') and \
       not hasattr(args, 'repo') and \
       not hasattr(args, 'secret'):
           print('Please provide proper arguments.')
           return True

    if args.extension is not None or \
       args.repo is not None or \
       args.secret is not None:
        if args.repo is None:
            print("--repo path required")
            return True
        elif args.extension is None:
            print("--extension required")
            return True
        elif args.secret is None:
            print("--secret required")
            return True
        elif args.secret is None:
            print("--secret required")
            return True
        template_manager.get_all_template_files(args.repo, args.extension,
                                                args.secret)
        return True
    return False
