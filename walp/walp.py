import click
import walp.scripts.collection as col
import walp.scripts.state as state
import walp.scripts.image as img


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


@cli.command(name="import")
@click.argument("input", type=click.Path(exists=True), nargs=-1)
def importFileOrDir(input):
    for image in input:
        if img.importImage(image) > 0:
            click.echo("Not imported (not an image)")
        else:
            click.echo("Wallpaper loaded correctly.")


# Group for collection interface commands
@cli.group(name="collection")
def collection():
    pass


@collection.command(name="list")
def collection_list():
    collections = col.list_collection_names()

    if len(collections) < 1:
        click.echo("No collections found!\n\nUse: walp collection create [NAME]\n to create a new collection.")
        return

    for i in collections:
        click.echo(i)


@collection.command(name="create")
@click.argument('collection_name')
def collection_create(collection_name):
    res = col.create_collection(collection_name)
    if res == 0:
        click.echo(f"New collection {collection_name} created successfully.")
    elif res == 1:
        click.echo("Collection could not be created. A collection with the same name already exists.")
    else:
        click.echo("Collection could not be created (problem unknown)")


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
