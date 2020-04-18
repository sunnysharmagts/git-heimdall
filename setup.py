"""Setup script."""

import setuptools

import heimdall

_requires = open('requirements-dev.txt').read().splitlines()
_long_description = open('README.rst').read()
_version = heimdall.__version__

setuptools.setup(name='git-heimdall',
                 version=_version,
                 description='Tool to scan staged files before commit and provide functionality to create configuration file from secret\
                    templates',
                 author='Sunny Sharma',
                 author_email='sunnysharmagts@gmail.com',
                 long_description=_long_description,
                 install_requires=_requires,
                 packages=setuptools.find_packages(),

                 entry_points={
                     'console_scripts': {
                         'heimdall=heimdall.manager:main'
                     }
                 },
                 include_package_data=True,
                 # Reference for classifiers: https://pypi.org/classifiers/
                 classifiers=[
                     'Development Status :: 2 - Pre-Alpha',
                     'Intended Audience :: Developers',
                     'Intended Audience :: End Users/Desktop',
                     'Intended Audience :: Information Technology',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 3',
                     'Topic :: System :: Monitoring',
                 ],
                )
