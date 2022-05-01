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

@click.command("collection")
def collection():
    click.echo("collection!")
