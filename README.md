# Home Automation Devices  

## Overview  

> This is a collection of [ESPHome](https://ESPHome.io) configuration files, [Tasmota](https://tasmota.github.io/docs/) dmp files and code for my various ESP8266 devices that integrate with [Home Assistant](https://www.home-assistant.io/). I am using includes and packages pretty extensively in order to prevent duplication and allow for easy changing of common settings.
> </br>
> **What is ESPHome?**  
> ESPHome is a system to control your ESP8266/ESP32 by simple yet powerful configuration files and control them remotely through Home Automation systems. For more information checkout [ESPHome.io](https://ESPHome.io).
> </br>
> **What is Tasmota?**  
> Total local control with quick setup and updates.
Control using MQTT, Web UI, HTTP or serial.
Automate using timers, rules or scripts.
Integration with home automation solutions.
Incredibly expandable and flexible. For more information checkout [Tasmota](https://tasmota.github.io/docs/).
> </br>
> **What is Shelly?**  
> Shelly is a collection of IoT devices that are built for home automation. For more information checkout [Shelly Cloud](https://shelly.cloud/).
> </br>
> **What is Home Assistant**
> Home Assistant is open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.  For more information check out [Home-Assistant.io](https://www.home-assistant.io/).

## Custom Devices

### Study

#### Octopi

I have a simple query that publishes data to a MQTT Topic and then captured by Node-Red and sent into Home-Assistant. My file to publish RPI Temperature to MQTT can be found [here](/python/temp1-hassos-mqtt.py). You would need to modify the required settings in the file, for example,  

1. MQTT Server
2. MQTT Username
3. MQTT Password
4. MQTT Topic

#### Study Sensor

#### [Server Cabinet Fan](/esphome/study/sonoff-powr2-server-cabinet.yaml)  

> This is a SonOff POW R2 based upon [ESPHome](esphome.io). Used by my [Home Automation System](https://www.home-assistant.io/) and [Node-Red](https://nodered.org/) for some great automations. I have a sensor in my server cabinet and it gathers temperature data, when the temperature goes over a set point, Node-Red will then turn on the server fan and then turn the fan back off after set conditions are met.

### Kitchen  

#### [Washing Machine SonOff POW](/esphome/kitchen/sonoff-powr2-washing-machine.yaml)  

This is a SonOff POW R2 based upon [ESPHome](esphome.io). Used by my [Home Automation System](https://www.home-assistant.io/) and [Node-Red](https://nodered.org/) for some great automations. Specifically for Power Monitoring and then using Alexa to tell us that the washing is complete. This is quite useful as we seem to have a tendency to forget. Have you ever smelled wahing that was left in a washing machine too long? :rage:

### Lounge  

#### [Lounge Light](/tasmota/lounge/Config_loungergbw_5090_9.1.0.dmp)

This lightbulb is based on [Tasmota](https://tasmota.github.io/docs/). Used by my [Home Automation System](https://www.home-assistant.io/) and [Node-Red](https://nodered.org/) for some great automations.  
The file can be found [here](/tasmota/lounge/Config_loungergbw_5090_9.1.0.dmp)  

### Garage

## Off the Shelf Devices

> ### [Basement Bathroom Sensor](./devices/basement_bathroom_sensor.yaml)

> This is a [WEMOS D1 Mini clone](https://www.amazon.com/gp/product/B076F52NQD/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) that is connected to a [motion sensor](https://www.amazon.com/gp/product/B07GJDJV63/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1), a [temperature/humidity/pressure sensor](https://www.amazon.com/gp/product/B07KYJNFMD/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1), and a [door sensor](https://www.amazon.com/gp/product/B07YBGZNNW/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) and is used to control the lights, fan, and heater (heat lamps in the fan) in my basement bathroom.
