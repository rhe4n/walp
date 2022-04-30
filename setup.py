from setuptools import setup

setup(
    name='walp',
    version='0.0.1',
    packages=["walp"],
    install_requires=[
        "Click"
    ],
    entry_points={
        'console_scripts': [
            'walp = walp:collection',
        ],
    },
)
