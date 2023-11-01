<div align="center">
<img src="https://github.com/razielar/RaspberryPi_dht22_vcgencmd_tig_docker/blob/main/img/raspberrypi_tig.png" alt="logo"></img>
</div>

# RaspberryPi: dht22, vcgencmd, TIG stack, and Docker

1. [Description](#ds)
2. [Getting Started](#gs)
    1. [DHT22](#dht22)
    2. [Grafana](#grafana)
3. [Contributing](#contributions)

## <a id='ds'></a> 1) Description

Monitor the temperature and humidity through the *DHT22 sensor* and Raspberry pi, using the TIG stack (Telegraf, Influxdb, Grafana) all with Docker and Docker-compose. Additionally, monitor telemetry data, and custom Raspberry Pi data using the stdout of `vcgencmd`. 

Further description can be found on my [Medium post](https://medium.com/@razielar/dockerizing-climate-telemetry-ac453891196d).

## <a id='gs'></a> 2) Getting Started

Clone the repo

```bash
git clone https://github.com/razielar/raspberrypi_dht22_tig.git
```

You must change the environment variables placed in `.env`, replace all **<ADD_YOUR_DATA>** with your desired variables

```bash
├── vcgencmd/
├── .env         <---
├── .gitignore
├── LICENSE
└── ...
```

Start the service

```bash
docker-compose up --build -d
```

### <a id='dht22'></a> DHT22

To capture temperature (by default Celsius, but you can change it on the `.env` file) and humidity readings from the Raspberry Pi, we need to connect the DHT22 sensor (with 3 pins) to the Pi, as shown in the following image:

<div align="center">
<img src="https://github.com/razielar/raspberrypi_dht22_vcgencmd_tig_docker/blob/main/img/dht22_connections.png" alt="logo"></img>
</div>

If you want to use the GPIO 4 of the Raspberry Pi, you will need to modify the script: `dht22/dht22_vcgencmd.py` as follows:

```python
dhtDevice = adafruit_dht.DHT22(board.D2, use_pulseio=False) # from board.D2 to board.D4
```

### <a id='grafana'></a> Grafana

By default, the username and password for Grafana are `admin` for both cases. 

When you connect, Grafana with Influxdb you need to consider two things:

* Query language: `Flux` (optional) but the Grafana dashboards (`grafana_dashboards/`) uses Flux.
* HTTP-URL: `http://influxdb:8086` defined within the `.env` file.

Grafana Dashboard for DHT22 sensor:

<div align="center">
<img src="https://github.com/razielar/raspberrypi_dht22_vcgencmd_tig/blob/main/img/graphana_dashboard_2.png" alt="logo"></img>
</div>

Grafana Dashboard for Raspberry Pi Telemetry:

<div align="center">
<img src="https://github.com/razielar/raspberrypi_dht22_vcgencmd_tig/blob/main/img/graphana_dashboard_1.png" alt="logo"></img>
</div>


## <a id='contributions'></a> 3) Contributing
Contributions are always welcome! 