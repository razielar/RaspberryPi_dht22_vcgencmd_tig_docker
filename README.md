<div align="center">
<img src="https://github.com/razielar/RaspberryPi_dht22_vcgencmd_tig_docker/blob/main/img/raspberrypi_tig.png" alt="logo"></img>
</div>

# RaspberryPi: dht22, vcgencmd, TIG stack, and Docker

1. [Description](#ds)
2. [Getting Started](#gs)
3. [Contributing](#contributions)
4. [Appendix](#app)

## <a id='ds'></a> 1) Description

Monitor the temperature and humidity through the *dht22 sensor* and raspberry pi, using the TIG stack (Telegraf, Influxdb, Grafana) all with docker and docker-compose. Additionally, monitor telemetry data, and custom raspberry pi data using the stdout of `vcgencmd`. 

Further description can be found in my [Medium post]().

## <a id='gs'></a> 2) Getting Started

Clone the repo

```bash
git clone https://github.com/razielar/raspberrypi_dht22_vcgencmd_tig.git
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

### DHT22

<div align="center">
<img src="https://github.com/razielar/raspberrypi_dht22_vcgencmd_tig_docker/blob/main/img/dht22_connections.png" alt="logo"></img>
</div>

## <a id='contributions'></a> 3) Contributing
Contributions are always welcome! 

## <a id='app'></a> 4) Appendix

If you wish to monitor other device (which is not a raspberry pi) using the TIG stack, or monitor the temperature and humidity without using vcgencmd, you can use the following branches: `telemetry` and `dht22`, respectively.