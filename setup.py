from setuptools import setup, find_packages


setup(
    name = 'CalculyFy',
    version = '1.0',
    packages = find_packages(),
    requires = ['colorama'],
    entry_points = {
        "console_scripts" : [
            'clc-check = calculyfy.cli:check',
            'clc-info = calculyfy.cli:dist_info'
        ],
    },
)