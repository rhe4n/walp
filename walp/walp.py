import click
import walp.scripts.collection as col
import walp.scripts.state as state


@click.group()
def cli():
    pass


@cli.command(name="status")
def showStatus():
    s = state.getState()
    if s["current"] == "none":
        click.echo("Status: Inactive")
    else:
        click.echo(f"Using {s['type']} '{s['current']}'")




# Group for collection interface commands
@cli.group(name="collection")
def collection():
    pass


@collection.command(name="list")
def collection_list():
    collections = col.list_collections()

    if len(collections) < 1:
        click.echo("No collections found!\n\nUse: walp collection create [NAME]\n to create a new collection.")
        return

    for i in collections:
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
