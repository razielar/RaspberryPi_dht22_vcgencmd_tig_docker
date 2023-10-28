<div align="center">
<img src="https://github.com/razielar/RaspberryPi_dht22_vcgencmd_tig_docker/blob/main/img/raspberrypi_tig.png" alt="logo"></img>
</div>

# RaspberryPi: dht22, vcgencmd, TIG stack, and Docker

Monitor the temperature and humidity through the *dht22 sensor* and raspberry pi, using the TIG stack (Telegraf, Influxdb, Grafana) all with docker and docker-compose. Additionally, monitor telemetry data, and custom raspberry pi data using the stdout of `vcgencmd`. 

If you wish to monitor other device (which is not a raspberry pi) using the TIG stack, or monitor the temperature and humidity without using vcgencmd, you can use the following branches: `telemetry` and `dht22`, respectively.

## Contributing
Contributions are always welcome! 