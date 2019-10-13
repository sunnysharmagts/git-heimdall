#!/usr/bin/env python

import setuptools

_requires = open('requirements_dev.txt').read().splitlines()

setuptools.setup(name='secretfy-template-creator',
    version='0.0',
    description='Tool to create file from secret templates',
    author='Sunny Sharma',
    author_email='sunnysharmagts@gmail.com',
    install_requires=_requires,

    entry_points={
        'console_scripts': {
            'secretfy = secretfy_template.manager:main'
        }
    },
)
