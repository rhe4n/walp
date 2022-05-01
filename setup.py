from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='walp',
    version='0.0.1',
    description="A command-line wallpaper manager",
    url="https://github.com/rhe4n/walp",
    packages=["walp"],
    install_requires=[
        "Click"
    ],
    entry_points={
        'console_scripts': [
            'collection = src/walp:collection',
        ],
    },
)
