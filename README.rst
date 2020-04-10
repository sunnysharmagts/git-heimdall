Git-Heimdall
=============

Git-Heimdall is a guardian/gatekeeper tool for scanning sensitive data before
committing files to github. It also provides functionality for creating
configuration files from existing template files.

.. image:: https://img.shields.io/badge/source-blue.svg?
   :target: https://github.com/sunnysharmagts/Secretfy-config-creator/tree/master/secretfy_template

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?
   :target: https://github.com/sunnysharmagts/Secretfy-config-creator/blob/master/LICENSE.md

Contents
--------

.. contents:: Table of Contents:
    :backlinks: none

What is Git-Heimdall?
----------------------

Git-Heimdall is a tool for scanning sensitive data before the staged files are
added to a commit. So, if a developer makes some changes in his repository and
tries to commit those changes via `git commit`, those files will be first
scanned by *Git-Heimdall* to check whether there are any sensitive data in those
changes and informs developer about it.

This process is automated. You don't have to run extra commands in order to scan those files. Infact those files are scanned automatically when git commit is called.


Why Git-Heimdall?
------------------

Committing sensitive data has been one of the most common vulnerabilities in
security world. Developers commit sensitive data and expose it to internet
without even realising about it.

This is where Git-Heimdall comes in. Git-Heimdall provides a set of functionalities like :-

- Scanning files before commit to track secrets
- Keep configuration files in template format so that there are less chances
  of everytime modifying the config file and committing of secrets.(`More about
  Git-Heimdall secretfy`_)


Installation
------------

This section provides quick steps of how to setup this tool.

1. Create a virtual Python environment and install Git-heimdall in it.

   .. code-block:: sh

    python3 -m venv vheimdall
    . vheimdall/bin/activate
    pip3 install secretfy-config-creator
    heimdall -i

2. Run Sanity test

   .. code-block:: sh

    heimdall secretfy -m

   The above command creates mock templates, secrets file at
   ``/tmp/git-heimdall`` directory. The ``-c`` or ``--config``
   option is for providing your config.yaml file.


More about Git-Heimdall secretfy
--------------------------------

git-heimdall provides ``secretfy`` option for generating config files
dynamically from your template files. The templates are nothing but
configuration files, which holds your configuration in mustache format.

``secretfy`` tool generates the required configuration file with help of secrets
file which would contain the real values required for actual config/properties
file.

Let's just say you have a set of configuration which you keep in a file
config.yaml, config.json, application.properties etc. These configuration might
have some highly sensitive information required to execute your project like
your user credentials, email, phone number, private key etc. Everytime, in your
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


Development
------------

This section describes how to set up a development environment for
Git-Heimdall. This section is useful for those who would like to contribute to
Git-Heimdall or run Git-Heimdall directly from its source.

We use primarily three tools to perform development on this project: Python 3,
Git, and Make. Your system may already have these tools. But if not, here are
some brief instructions on how they can be installed.

1. On macOS, if you have `Homebrew <https://brew.sh/>`_ installed, then these tools can be be installed easily with the following command:

   .. code-block:: sh

    brew install python git

   On a Debian GNU/Linux system or in another Debian-based Linux distribution, they can be installed with the following commands:

   .. code-block:: sh

    apt-get update
    apt-get install python3 python3-venv git make

   On any other system, we hope you can figure out how to install these tools yourself.

2. Clone the project repository and enter its top-level directory:

   .. code-block:: sh

    git clone https://github.com/sunnysharmagts/Secretfy-config-creator
    cd Secretfy-config-creator

3. Create a virtual Python environment for development purpose:

   .. code-block:: sh

    make vheimdall deps

   This creates a virtual Python environment at ``~/.vheimdall/git-heimdall``.
   Additionally, it also creates a convenience script named ``vheimdall`` in
   the current directory to easily activate the virtual Python
   environment which we will soon see in the next point.

   To undo this step at anytime in future, i.e., delete the virtual
   Python environment directory, either enter
   ``rm -rf vheimdall ~/.vheimdall/``.

4. Activate the virtual Python environment:

   .. code-block:: sh

    . ./vheimdall

5. In the top-level directory of the project, enter this command:

   .. code-block:: sh

    python3 -m secretfy_template -i

   This initializes git-heimdall tool. This is just a **one time process** and
   need not be run everytime, unless if there is any change in the template
   resources. This command just updates in the location of the git templateDir
   in git configuration.

   .. code-block:: sh

    python3 -m secretfy_template secretfy -m

   This generates mock data at ``/tmp/git-heimdall``. This step serves as a
   sanity check that ensures that the development environment is correctly set
   up. Also, it gives a brief idea of how to create a config in form of
   template.

6. Now to simulate the environment and test the tool. Do the following:-

   .. code-block:: sh

    . ~/.vheimdall/git-heimdall/bin/activate
    mkdir /tmp/git-heimdall-tool-test
    cd /tmp/git-heimdall-tool-test
    echo -n "print('<insert-some-sensitive-value>')" >> sample.py
    git init
    git add .
    git commit -m "Sample commit"

   This will start scanning the sample.py file and will provide you with the sensitive data that you have in this file. Add more files and play with the tool to familiar yourself.


How to Use
----------

This section provides samples of how to use this tool.

``heimdall secretfy`` consist of 3 components :-

**Secrets file** - This file can be in yaml, json and xml format.

**Template files** - These files are configuration files in template format. For
eg:- If you have a file `config.json` then your template file will be
`config.json.mustache`.

**Extension** - This is the file extension of your configuration file. Following
are the example config files and their respective extension.

.. code-block:: sh

  a. config.yaml       : yaml
  b. config.xml        : xml
  c. config.json       : json
  d. config.properties : properties

These parameters can be added to a ``baseconfig.yaml`` file in the following way

.. code-block:: sh

  secretfy_template:
      secret: res/secrets.yaml
      templates:
          -
            file: res/example.yaml.mustache
            extension: yaml
          -
            file: res/example.json.mustache
            extension: json
          -
            file: res/example.xml.mustache
            extension: xml


The ``baseconfig.yaml`` file starts with ``secretfy_template`` tag.

1. ``secret`` is the absolute path of the secrets file containing sensitive
values.

2. ``templates`` tag is an array of template files. All these files are in
``.mustache`` format whose sensitive values resides in ``secrets.yaml`` file.

* ``file`` is the absolute path of the template file.
* ``extension`` is the extension of the configuration file which will be
  generated from the template file.

``NOTE: Make sure that the template file are in <file_name>.<extension>.<mustache> format.``

Run the following command to generate the config files.

.. code-block:: sh

  heimdall secretfy -c baseconfig.yaml

This will create config files in the respective directories. Note that these
configurations won't be seen in git history. You can check that by doing ``git
status``.


Config template file samples
----------------------------

**secrets.yaml**

.. code-block:: sh

  secrets:
      item:
          val1: foo@bar.com
          val2: my_password
      item1:
          val3: username
          val4: my_private_key


**example.yaml.mustache**

.. code-block:: sh

  secrets:
    item:
        val1: {{secrets.item.val1}}
        val2: {{secrets.item.val2}}
        result: This is just a dummy description.
    item1:
        val3: {{secrets.item1.val3}}
        val4: {{secrets.item1.val4}}
        result: This is another dummy description.


The `secrets.yaml` file contains the sensitive information and
`example.yaml.mustache` is the template file which contains the keys in
`mustache` format. Hence the key `secrets.item.val2` has value `my_password`
which will be populated via `heimdall secretfy` tool.

``NOTE: You can run `heimdall secretfy -m` to get more sample baseconfig, templates, secret files. These files will get generated at `/tmp/git-heimdall`.``


FAQ
---

**How can i deploy my code in CICD pipeline or on remote server since it
doesn't have config files and needs to be generated.**

You can generate all the config files required for your repository to compile
and run in CICD pipeline or at remote server by the following command.

.. code-block:: sh

  heimdall secretfy -e mustache -s <secrets_file_path> -r <repository_path>

``-e`` is the template extension, ``-s`` is the absolute path of the secrets file
and ``-r`` is absolute path of the repository


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
