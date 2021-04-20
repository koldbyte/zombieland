"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Zombieland."""


if __name__ == "__main__":
    main(prog_name="zombieland")  # pragma: no cover
