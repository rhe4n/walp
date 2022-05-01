from . import walp
from walp.utils import storage

def main():
    storage.init()
    walp.cli()
