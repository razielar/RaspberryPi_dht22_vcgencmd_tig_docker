#!/usr/bin/env python
#coding=utf8
"""
Author: Raziel Amador Rios
Version: 0.0.1
"""
import os
import time
from typing import List
import board
import adafruit_dht
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# vars
PORT = os.environ['DOCKER_INFLUXDB_INIT_PORT']
URL = f"http://{os.environ['DOCKER_INFLUXDB_INIT_HOST']}:{PORT}"
TOKEN = os.environ['DOCKER_INFLUXDB_INIT_ADMIN_TOKEN']
ORG = os.environ['DOCKER_INFLUXDB_INIT_ORG']
BUCKET = os.environ['DOCKER_INFLUXDB_INIT_BUCKET']
DELAY = os.environ["DHT_VCGENCM_INTERVAL"]
VCGENCMD_DATA = os.environ["VCGENCMD_DATA"]
TEMPERATURE_UNIT = os.environ["TEMPERATURE_UNIT"]

def _log_influxdb(url: str, token: str, org: str, bucket: str, sensor_type: str, values: List[float]) -> None:
    """
    Log the data to influxdb 2.0
    Args:
        sensor_type: either dht22 (i.e. temperature and humidity) or vcgencm (i.e. soc_temp, etc.)
    """
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    if sensor_type == "dht22":
        p = Point("flat_iot").tag("location", "living_room").field("temperature", values[0]).field("humidity", values[1])
    elif sensor_type == "vcgencm":
        p = Point("vcgencm").field("cpu_clock", values[0]).field("cpu_voltage", values[1]).field("soc_temp", values[2])
    write_api.write(bucket=bucket, org=org, record=p)

def _vcgencm(volume_path: str) -> None:
    """
    Get and log: the vcgencm stdout from the vcgencm container, reading the last line from the tsv file.
    Args:
        volume_path: the path of the vcgencm container
    """
    with open(volume_path, "r") as tsv_file:
        lines = tsv_file.readlines()
        if lines:
            last_line = lines[-1]
            data = last_line.strip().split('\t')
            cpu_clock = float(data[0])
            cpu_voltage = float(data[1])
            soc_temp = float(data[2])
            _log_influxdb(url=URL, token=TOKEN, org=ORG, bucket=BUCKET, sensor_type="vcgencm", values=[cpu_clock, cpu_voltage, soc_temp])

def main(delay: float, condition: bool=True) -> None:
    """
    Get and log: Temperature & Humidity from the dht22 sensor and vcgencm stdout.
    Args:
        delay (seconds): how often you want to read the data 
    """
    dhtDevice = adafruit_dht.DHT22(board.D2, use_pulseio=False)
    while condition:
        try:
            _vcgencm(volume_path= VCGENCMD_DATA)
            humidity = dhtDevice.humidity
            if TEMPERATURE_UNIT == "Celsius":
                temperature = dhtDevice.temperature
            elif TEMPERATURE_UNIT == "Fahrenheit":
                temperature = dhtDevice.temperature * (9 / 5) + 32
            _log_influxdb(url=URL, token=TOKEN, org=ORG, bucket=BUCKET, sensor_type="dht22", values=[temperature, humidity])
        except RuntimeError as error:
            time.sleep(delay)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        time.sleep(delay)

if __name__ == "__main__":
    main(delay=float(DELAY))