import click

@click.command()
@click.option('--name')
@click.option('--firstname', is_flag=True)
@click.option('--lastname', is_flag=True)
def cli(name, firstname, lastname):
    first, last = name.split()
    if firstname:
        click.echo(first)
    elif lastname:
        click.echo(last)

if __name__ == '__main__':
        cli()
