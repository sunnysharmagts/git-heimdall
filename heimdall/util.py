#!/usr/bin/env python

import argparse
import logging
import os
import sys

import yaml

import heimdall
from heimdall import config

_log = logging.getLogger(__name__)


def parse_cli(args=None):
    """Parse command line arguments.

    Arguments:
        args (list): List of command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.

    """

    parser = argparse.ArgumentParser(prog='heimdall')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s' + heimdall.__version__)

    parser.add_argument(
        '-scan',
        '--codescan',
        nargs='*',
        help='your project\'s absolute path')

    parser.add_argument(
        '-i',
        '--init',
        action='store_true',
        help='Initialize Heimdall tool')

    parser.add_argument(
        '-reg',
        '--register',
        nargs='*',
        help='Register repository for heimdall scan')

    parser.add_argument(
        '-un-reg',
        '--un-register',
        nargs='*',
        help='Un-register repository from heimdall scan')

    _heimdall_sub_parser = parser.add_subparsers()

    _secretfy_parser = _heimdall_sub_parser.add_parser('secretfy',
                                                       help='secretfy command')
    add_secretfy_arguments(_secretfy_parser)
    args = parser.parse_args(args)

    return args


def add_secretfy_arguments(parser):

    absolute_path = config.get_config_path()
    default_config_paths = [
        absolute_path + '/baseconfig.yaml',
        absolute_path + '/baseconfig1.yaml',
    ]

    parser.add_argument(
        '-c',
        '--config',
        nargs='*',
        default=default_config_paths,
        help='generates config file with provided configuration params')

    parser.add_argument(
        '-m',
        '--mock',
        action='store_true',
        help='generate mock config file with mock configuration \
            param at /tmp/git-heimdall')

    parser.add_argument(
        '-e',
        '--extension',
        nargs='*',
        help='extension of the template files')

    parser.add_argument(
        '-s',
        '--secret',
        nargs='*',
        help='secret file path')

    parser.add_argument(
        '-r',
        '--repo',
        nargs='*',
        help='your project\'s absolute path')


def load_config(config_paths):
    """Load configuration from specified configuration paths.

    Arguments:
        config_paths (list): Configuration paths.

    Returns:
        dict: A dictionary of configuration key-value pairs.

    """
    new_config = None
    for config_path in config_paths:
        config_path = os.path.expanduser(config_path)
        _log.info('Looking for %s', config_path)
        if not os.path.isfile(config_path):
            continue

        _log.info('Found %s', config_path)
        with open(config_path) as f:
            new_config = yaml.safe_load(f)
            new_config = new_config['heimdall']
    if not isinstance(new_config, list):
        new_config = [new_config]
    return new_config
