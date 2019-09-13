import click


@click.group()
def cli():
    pass


@cli.command('name')
@click.argument('name1', nargs=-1, required=True)
@click.option('--firstname', default='1', nargs=0)
@click.option('--lastname', default='b', nargs=0)
def name(name1, firstname, lastname):

    if not firstname:
        click.echo(name1[0])
    elif not lastname:
        click.echo(name1[-1])
    else:
        click.echo(' '.join(name1))


if __name__ == '__main__':
        cli()
