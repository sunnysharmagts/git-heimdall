"""Setup script."""

import setuptools
import secretfy_template

_requires = open('requirements-dev.txt').read().splitlines()
_version = secretfy_template.__version__

setuptools.setup(name='secretfy-template-creator',
                 version=_version,
                 description='Tool to create configuration file from secret\
                    templates',
                 author='Sunny Sharma',
                 author_email='sunnysharmagts@gmail.com',
                 install_requires=_requires,
                 packages=setuptools.find_packages(),

                 entry_points={
                     'console_scripts': {
                         'secretfy=secretfy_template.manager:main'
                     }
                 },
                 )
