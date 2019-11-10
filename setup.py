"""Setup script."""

import setuptools
import secretfy_template

_requires = open('requirements-dev.txt').read().splitlines()
_long_description = open('README.rst').read()
_version = secretfy_template.__version__

setuptools.setup(name='secretfy-config-creator',
                 version=_version,
                 description='Tool to create configuration file from secret\
                    templates',
                 author='Sunny Sharma',
                 author_email='sunnysharmagts@gmail.com',
                 long_description=_long_description,
                 install_requires=_requires,
                 packages=setuptools.find_packages(),

                 entry_points={
                     'console_scripts': {
                         'secretfy=secretfy_template.manager:main'
                     }
                 },
                 include_package_data=True,
                 )
