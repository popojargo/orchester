import click
import sys
from orchester import ConfigHelper, ConfigEntryMissingError
from orchester.ConfigHelper import pick
from orchester.ConnectorManager import ConnectorManager, ConnectorType
from orchester.Exceptions import ConfigFileNotFoundError, RequestFailedError
from orchester.utils import gen_gdrive_token, gen_slack_token, gen_trello_token

config = None
default_connector = None
SUPPORTED_GEN_CONNECTOR = ['trello', 'slack', 'g_drive']


def safe_wrapper(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConfigEntryMissingError as e:
            click.echo(e)
            exit(1)
        except ConfigFileNotFoundError as e:
            click.echo(e)
            exit(1)
        except RequestFailedError as e:
            click.echo(e)
            exit(1)

    return func_wrapper


@safe_wrapper
def preprocess():
    global config, default_connector
    config = ConfigHelper.get_config_data()
    default_connector = pick(config, 'default_connector') if 'default_connector' in config else ""


preprocess()


def get_connector_type(ctx):
    connector = ctx.obj['CONNECTOR']
    if not connector:
        click.echo('You must supply a connector type')
        exit(1)
    return ConnectorType(connector)


@click.group()
@click.option('--connector', '-c', help='The connector name', type=click.STRING, default=default_connector)
@click.pass_context
def cli(ctx, connector):
    if not ctx.obj:
        ctx.obj = {}
    ctx.obj['CONNECTOR'] = connector


@cli.command()
@click.argument('identifier', type=click.STRING)
@click.pass_context
def check(ctx, identifier):
    manager = ConnectorManager(config)
    connector_type = get_connector_type(ctx)
    click.echo(manager.is_registered_to_group(connector_type, identifier))


@cli.command()
@click.argument('identifier', type=click.STRING)
@click.pass_context
def add(ctx, identifier):
    manager = ConnectorManager(config)
    connector_type = get_connector_type(ctx)
    click.echo(manager.add_to_group(connector_type, identifier))


@cli.command()
@click.argument('identifier', type=click.STRING)
@click.pass_context
def rm(ctx, identifier):
    manager = ConnectorManager(config)
    connector_type = get_connector_type(ctx)
    click.echo(manager.remove_from_group(connector_type, identifier))


@cli.command()
@click.argument('connector')
def generate(connector):
    if not connector in SUPPORTED_GEN_CONNECTOR:
        msg = "Unsupported connector for token generation. Choose one from: {}".format(
            ','.join(SUPPORTED_GEN_CONNECTOR))
        click.echo(msg)
        exit(1)
    if connector == 'trello':
        gen_trello_token.generate()
    elif connector == 'slack':
        gen_slack_token.generate()
    elif connector == 'g_drive':
        # We have to reset the arguments otherwise the generation fails
        sys.argv = [sys.argv[0]]
        gen_gdrive_token.generate()


@safe_wrapper
def main():
    cli(obj={})


if __name__ == '__main__':
    main()
