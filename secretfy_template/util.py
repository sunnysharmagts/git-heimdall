#!/usr/bin/env python

import logging
import os
import yaml
import argparse
from secretfy_template import config
import secretfy_template
import ntpath

_log = logging.getLogger(__name__)


def parse_cli(args=None):
    """Parse command line arguments.

    Arguments:
        args (list): List of command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.

    """
    absolute_path = config.get_config_path()
    default_config_paths = [
        absolute_path + '/baseconfig.yaml',
        absolute_path + '/config.yaml',
    ]
    parser = argparse.ArgumentParser(prog='secretfy')

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
            param at /tmp/secretfy-config-creator')

    parser.add_argument('-v', '--version', action='version',
    version='%(prog)s' + secretfy_template.__version__)

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

    args = parser.parse_args(args)
    return args


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
            new_config = new_config['secretfy_template']
    if not isinstance(new_config, list):
        new_config = [new_config]
    return new_config
