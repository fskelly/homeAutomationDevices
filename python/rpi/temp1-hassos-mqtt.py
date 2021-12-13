#!/usr/bin/python

# Copyright (c) 2013-2014 Beebotte <contact@beebotte.com>
# This program is published under the MIT License (http://opensource.org/licenses/MIT).

############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
#############################################################

import time
import paho.mqtt.client as mqtt
from subprocess import check_output
from re import findall


# Will be called upon reception of CONNACK response from the server.
def on_connect(client, data, flags, rc):
    client.subscribe("mychannel/myresource", 1)

def on_message(client, data, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set the username to 'token:CHANNEL_TOKEN' before calling connect
client.username_pw_set('mqtt', password='')
# Alternatively, set the username to your SECRET KEY
#client.username_pw_set('YOUR_SECRET_KEY')
client.connect("192.168.1.200", 1883, 60)

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

temp = get_temp()


##client.loop_start()

##while 1:
    # Publish a message every second
client.publish("home/rpi3/ender3control/temp", temp, 1)
time.sleep(1)
