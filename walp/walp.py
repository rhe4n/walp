import click


@click.group()
def cli():
    pass


@cli.command()
def collection():
    print("collection list")

