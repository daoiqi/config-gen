#!/usr/bin/env python

from setuptools import setup

setup(
    name='Config-gen',
    version=__import__('gencfg').__version__,
    description='Utility to generate configuration files',
    author='Samuele Santi',
    author_email='samuele@samuelesanti.com',
    url='https://github.com/rshk/config-gen',
    license='GNU General Public License v3 or later (GPLv3+)',
    scripts=['gencfg.py'],
    data_files=['README.rst', 'LICENSE'],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Utilities",
    ],
    install_requires=[
        "cool_logging",
        "jinja2",
    ],
    entry_points={
        'console_scripts': [
            'confgen-render = config_gen.commands.render:command',
            'confgen-quickstart = config_gen.commands.quickstart:command',
        ],
    },
)
