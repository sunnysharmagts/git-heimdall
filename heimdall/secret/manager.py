#!/usr/bin/env python


"""Manager of secrets file format

This module manages the file format of the secrets provided. The secrets can be
of any format which includes xml, json, yaml. For each format there is a
concret secret implementation which parses the secrets file and returns data in
dict format
"""


from heimdall.secret import secret


class SecretsManager:
    """ Secrets file manager plugin."""

    def get_secret(self, file):
        """Parses the secrets file and returns a dict of data of secrets file.

        It checks the file format of the provided secrets file and based on
        that create an instance of secrets file processor which and sends to
        secrets file to it to be parsed.

        Arguments:
            file (str): absolute path of secrets file.

        Returns:
            dict: Secrets file data.
        """
        s = None
        if file.endswith('.xml'):
            s = secret.XmlSecret()
        elif file.endswith('.yaml') or file.endswith('.json'):
            s = secret.YamlJsonSecret()

        secrets_file = open(file, 'r')
        return s.get_secret(secrets_file)
