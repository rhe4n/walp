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
        "click>=8.0.3",
        "appdirs>=1.4.4"
    ],
    entry_points={
        "console_scripts": [
            "walp = walp:main",
        ],
    },
    package_data={
        "walp": ["dirs.dat"]
    }
)
