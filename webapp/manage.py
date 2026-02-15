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
def migrate():
    """Apply database migrations."""
    click.echo("Applying migrations...")


@cli.command()
def createsuperuser():
    """Create a superuser account."""
    #click.echo("Creating superuser...")
    pass

@cli.command()
def help():
    """Show this help message."""
    click.echo(cli.get_help(click.Context(cli)))


@cli.command(name="docker-dev-up")
def docker_dev_up():
    """Start Docker Compose (prefers `docker compose`, falls back to `docker-compose`)."""
    import shutil, subprocess, sys, os

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    compose_file = os.path.join(project_root, "infra", "docker", "dev", "docker-compose.yml")
    env_file = os.path.join(project_root, ".env")

    if not os.path.exists(compose_file):
        click.echo(f"Error: docker-compose file not found: {compose_file}")
        sys.exit(1)

    if not os.path.isfile(env_file):
        click.echo(f"Error: .env file not found at project root: {env_file}")
        sys.exit(1)

    docker_bin = shutil.which("docker")
    compose_bin = shutil.which("docker-compose")

    # Prefer `docker compose`
    if docker_bin:
        try:
            subprocess.run([docker_bin, "compose", "version"], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            click.echo("Using 'docker compose'...")
            subprocess.run([docker_bin, "compose", "-f", compose_file, "up", "-d"], check=True, cwd=project_root)
            click.echo("Docker Compose swarm started.")
            return
        except subprocess.CalledProcessError:
            pass

    # Fallback to docker-compose
    if compose_bin:
        if compose_bin.startswith("/mnt/") or "Program Files" in compose_bin:
            click.echo("Warning: docker-compose is from a Windows path. Enable Docker Desktop WSL integration or install Docker in WSL.")
        click.echo("Using 'docker-compose'...")
        try:
            subprocess.run([compose_bin, "-f", compose_file, "up", "-d"], check=True, cwd=project_root)
            click.echo("Docker Compose swarm started.")
            return
        except subprocess.CalledProcessError as e:
            click.echo(f"docker-compose failed: {e}")
            sys.exit(e.returncode)

    click.echo("Error: neither 'docker compose' nor 'docker-compose' found in PATH.")
    click.echo("On WSL2: enable Docker Desktop WSL integration or install Docker + compose plugin in this distro.")
    sys.exit(1)

if __name__ == "__main__":
    cli()
