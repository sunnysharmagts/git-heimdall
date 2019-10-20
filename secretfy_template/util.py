#!/usr/bin/env python

import logging
import os
import yaml

_log = logging.getLogger(__name__)


def parse_cli(args=None):
    """Parse command line arguments.

    Arguments:
        args (list): List of command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.

    """


def load_config():
    """Load configuration from specified configuration paths.

    Arguments:
        config_paths (list): Configuration paths.

    Returns:
        dict: A dictionary of configuration key-value pairs.

    """
    default_config_paths = [
        '~/.secretfy_config.yaml',
        'secretfy_config.yaml',
    ]
    new_config = None
    for config_path in default_config_paths:
        config_path = os.path.expanduser(config_path)
        _log.info('Looking for %s', config_path)

        if not os.path.isfile(config_path):
            continue

        _log.info('Found %s', config_path)
        with open(config_path) as f:
            new_config = yaml.safe_load(f)
            new_config = new_config['secretfy_template']
            break

    return new_config
