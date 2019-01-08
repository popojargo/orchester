import click
from ConnectorManager import ConnectorManager, ConnectorType

manager = ConnectorManager()

@click.group()
def main():
    pass


@main.command()
@click.argument('connector', type=click.STRING, required=True, )
@click.argument('username', type=click.STRING)
def check(connector, username):
    connector_type = ConnectorType(connector)
    click.echo(manager.is_registered_to_group(connector_type, username))


@main.command()
@click.argument('connector', type=click.STRING, required=True, )
@click.argument('username', type=click.STRING)
def add(connector, username):
    connector_type = ConnectorType(connector)
    click.echo(manager.add_to_group(connector_type, username))


@main.command()
@click.argument('connector', type=click.STRING, required=True, )
@click.argument('username', type=click.STRING)
def rm(connector, username):
    connector_type = ConnectorType(connector)
    click.echo(manager.remove_from_group(connector_type, username))


if __name__ == '__main__':
    main()