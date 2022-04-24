"""Console script for images_to_pdf."""
import sys
import click


@click.command()
@click.argument('image_files', nargs=-1, type=click.File('r'))
def main(image_files):
    """Console script for images_to_pdf."""
    print(image_files)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
