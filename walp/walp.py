import click
import walp.scripts.collection as col
import walp.scripts.preset as pres
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


@cli.command(name="use")
@click.argument("type", type=click.Choice(case_sensitive=False, choices=["preset", "collection"]))
@click.argument("name", type=click.STRING)
def useSaved(type, name):
    if type == "preset":
        pres.use_preset(name)
    elif type == "collection":
        col.use_collection(name)


# Group for collection interface commands
@cli.group(name="collection")
def collection():
    pass


@collection.command(name="delete")
@click.argument("collection_name")
def collection_delete(collection_name):
    res = col.delete_collection(collection_name)
    if res == 0:
        click.echo(f"Collection {collection_name} deleted successfully.")
    elif res == 1:
        click.echo("Collection could not be deleted (not found).")
    else:
        click.echo("Collection could not be created (problem unknown)")


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


# Group for preset interface commands
@cli.group(name="preset")
def preset():
    pass


@preset.command(name="create")
@click.argument('preset_name')
def preset_create(preset_name):
    res = pres.create_preset(preset_name)
    if res == 0:
        click.echo(f"New preset {preset_name} created successfully.")
    elif res == 1:
        click.echo("Preset could not be created. A preset with the same name already exists.")
    else:
        click.echo("Preset could not be created (problem unknown)")


@preset.command(name="delete")
@click.argument("preset_name")
def preset_delete(preset_name):
    res = pres.delete_preset(preset_name)
    if res == 0:
        click.echo(f"Preset {preset_name} deleted successfully.")
    elif res == 1:
        click.echo("Preset could not be deleted (not found).")
    else:
        click.echo("Preset could not be created (problem unknown)")


@preset.command(name="list")
def preset_list():
    presets = pres.list_preset_names()

    if len(presets) < 1:
        click.echo("No presets found!\n\nUse: walp preset create [NAME]\n to create a new preset.")
        return

    for i in presets:
        click.echo(i)


@preset.command(name="set")
@click.argument("preset_title", type=click.STRING)
@click.argument("image_title", type=click.STRING)
@click.argument("monitor_number", type=click.INT)
def preset_set_image_monitor(preset_title, image_title, monitor_number):
    res = pres.set_image_monitor(preset_title, image_title, monitor_number)

    if res == 0:
        click.echo("Image successfully assigned to monitor.")
    elif res == 1:
        click.echo("Error: This preset does not exist. Use 'walp preset create [name]' to create a preset.")
    elif res == 2:
        click.echo("Error: This image is not stashed. Use 'walp import [path]' to import images.")
    elif res == 3:
        click.echo("Error: Monitor needs to be greater than zero.")
    else:
        click.echo("Unknown error.")
