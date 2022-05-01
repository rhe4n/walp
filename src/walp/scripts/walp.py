"""
                .__
__  _  _______  |  | ______
\ \/ \/ /\__  \ |  | \____ \
 \     /  / __ \|  |_|  |_> >
  \/\_/  (____  /____/   __/
              \/     |__|

W.A.L.P.
"""
import click


@click.group("cli")
def cli():
    pass


@click.command("collection")
def collection():
    click.echo("collection!")


@click.command("preset")
def preset():
    click.echo("preset!")


cli.add_command(collection)
cli.add_command(preset)
cli()

# def main():
#     cli.add_command(collection)
#     cli.add_command(preset)
#     cli()
#
#
# if __name__ == "__main__":
#     main()
