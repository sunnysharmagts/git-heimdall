#!/usr/bin/env python


"""Secrets file processor

This module defines the skeleton of reading different file format and their
concrete implementation
"""

import xmltodict
import yaml


class Secret:
    """ Secret file processor abstraction. """

    def get_secret(self, file):
        """Abstract method for parse secrets file and return the data

        """
        raise NotImplementedError("Should implement secrets method.")
        pass


class XmlSecret(Secret):
    """ XML file format processor. """

    def get_secret(self, file):
        """Parse provided secrets xml file

        Arguments:
            file (_io.TextIOWrapper): secrets file to be parsed
        """
        return xmltodict.parse(file.read())


class YamlJsonSecret(Secret):
    """ Yaml and json file format processor. """

    def get_secret(self, file):
        """Parse provided secrets yaml and json file

        Arguments:
            file (_io.TextIOWrapper): secrets file to be parsed
        """
        return yaml.safe_load(file)
