import click
from walp.scripts.collection import list_collections
from walp.utils import storage


@click.group()
def cli():
    pass


@cli.command(name="status")
def showStatus():
    click.echo("active")


# Group for collection interface commands
@cli.group(name="collection")
def collection():
    pass


@collection.command(name="list")
def collection_list():
    for i in list_collections():
        click.echo(i)



@collection.command(name="create")
@click.argument('collection_name')
def collection_create(collection_name):
    print(f"creating collection {collection_name}")


@collection.command(name="add")
def collection_add():
    print("adding collection")


# Group for preset interface commands
@cli.group(name="preset")
def preset():
    pass


@preset.command(name="list")
def preset_list():
    print("preset1, preset2")
