Secretfy-config-creator
=======================

Secretfy-config-creator is a tool for creating configuration files from
existing template files.

.. image:: https://img.shields.io/badge/source-blue.svg?
   :target: https://github.com/sunnysharmagts/Secretfy-config-creator/tree/master/secretfy_template

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?
   :target: https://github.com/sunnysharmagts/Secretfy-config-creator/blob/master/LICENSE.md

Contents
--------

.. contents:: Table of Contents:
    :backlinks: none

What is Secretfy-config-creator?
--------------------------------

Secretfy-config-creator is a tool for generating config files dynamically from
your template files, without worrying about committing any sensitive data which
resides in your configuration file to github. The templates are also
configuration files, just that the sensitive values in the config file are
replaced by mustache object. The secretfy-config-creator tool generator the
required configuration file with help of secrets file which would contain the
real sensitive values required for actual config file.

Why Secretfy-config-creator?
----------------------------
Let's just say you have a set of configuration which you keep in a file
config.yaml or config.json. These configuration might have some highly
sensitive information required to execute your project like your user
credentials, email, phone number, private key etc. Everytime, in your
development process, you need to add these sensitive values to the config file
and remove them before committing the code into github.

This process is pretty painful and often you endup committing one or the other
sensitive information to git.

So, instead of having a config file, you can have a template which resembles
your config file. Now before executing your project. All you need to do is
generate the desired config file with the help of this tool and then follow the
usual approach of running the project. The best part is that you don't have to
worry about accidently commit the actual config file to the git repo. That file
won't be shown in git status unless you forcibly add it.

Install
-------

This section provides quick steps of how to setup this tool.

1. Create a virtual Python environment and install Secretfy-config-creator in it.

   .. code-block:: sh

    virtualenv vsecretfy
    source vsecretfy/bin/activate
    python3 setup.py install

2. Run Sanity test

   .. code-block:: sh

    secretfy -m

   The above command creates mock templates, secrets file at
   ``/tmp/secretfy-config-creator`` directory. The ``-c`` or ``--config``
   option is for providing your config.yaml file.


Support
-------

To report bugs, suggest improvements, or ask questions, please create a
new issue at https://github.com/sunnysharmagts/Secretfy-config-creator/issues.


License
-------

This is free software. You are permitted to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of it, under the
terms of the MIT License. See `LICENSE.md`_ for the complete license.

This software is provided WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
`LICENSE.md`_ for the complete disclaimer.

.. _LICENSE.md: https://github.com/sunnysharmagts/Secretfy-config-creator/blob/master/LICENSE.md
