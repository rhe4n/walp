from setuptools import setup


setup(
    name="walp",
    version="0.0.1.dev1",
    description="A command-line wallpaper manager",
    url="https://github.com/rhe4n/walp",
    author="rhean",
    author_email="rheandhont@gmail.com",
    packages=["walp"],
    install_requires=[
        "Click>=8.0.3",
    ],
    entry_points={
        "console_scripts": [
            "walp = walp:collection",
        ],
    },
)
