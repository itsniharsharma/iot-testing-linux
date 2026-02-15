import click
import yaml
from rich import print
from engines.mqtt_engine import run_mqtt_test

@click.group()
def cli():
    pass

@cli.command()
@click.argument("config")
def run(config):
    print("[cyan]Loading config...[/cyan]")

    with open(config) as f:
        cfg = yaml.safe_load(f)

    device = cfg["device"]
    rules = cfg["rules"]

    print("[green]Device Protocol:[/green]", device["protocol"])
    print("[green]Broker:[/green]", device["broker"])
    print("[green]Topic:[/green]", device["topic"])

    if device["protocol"] == "mqtt":
        run_mqtt_test(device, rules)

if __name__ == "__main__":
    cli()