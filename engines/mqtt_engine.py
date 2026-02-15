"""MQTT engine placeholder."""

import paho.mqtt.client as mqtt
import json
import time
from rich import print
from validators.rules import validate_packet

last_time = None
packet_count = 0

def run_mqtt_test(device, rules):

    def on_message(client, userdata, msg):
        global last_time, packet_count

        now = time.time()
        packet_count += 1

        try:
            data = json.loads(msg.payload)
        except:
            print("[red]Invalid JSON[/red]")
            return

        interval = None
        if last_time:
            interval = now - last_time
        last_time = now

        errors = validate_packet(data, rules, interval)

        if errors:
            print(f"[red]Packet {packet_count} FAIL[/red]", errors)
        else:
            print(f"[green]Packet {packet_count} PASS[/green]", data)

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(device["broker"])
    client.subscribe(device["topic"])

    print("[yellow]Listening for device data...[/yellow]")
    client.loop_forever()
