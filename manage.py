#!/usr/bin/env python3
import click


@click.group()
def cli():
    """Oort App Management CLI

    Commands:
      runserver         Run the development server
      migrate           Apply database migrations
      createsuperuser   Create a superuser account
      help              Show this help message
    """
    pass


@cli.command()
@click.option('--host', default=None, help='Host address')
@click.option('--port', default=None, help='Port number')
def runserver(host, port):
    """Run the development server."""
    click.echo(f"Starting development server at http://{host or '[default]'}:{port or '[default]'} ...")
    import os
    cmd = ["python", "main.py"]
    if host is not None:
        cmd.extend(["--host", str(host)])
    if port is not None:
        cmd.extend(["--port", str(port)])
    os.system(" ".join(cmd))


@cli.command()
def migrate():
    """Apply database migrations."""
    click.echo("Applying migrations...")


@cli.command()
def createsuperuser():
    """Create a superuser account."""
    click.echo("Creating superuser...")


@cli.command()
def help():
    """Show this help message."""
    click.echo(cli.get_help(click.Context(cli)))


if __name__ == "__main__":
    cli()