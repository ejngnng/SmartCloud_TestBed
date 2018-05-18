#!/usr/bin/env python
#-*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import requests
import json
import time

mqttBroker = "www.futuresmart.top"
pubTopic = ['device/device_register', 'device/status_update', 'device/status_reply']

def pub(msg):
	client = mqtt.Client()
	client.connect(mqttBroker)
	client.publish(pubTopic[2], msg)
	client.loop_forever()

def main():
	pub("hello world")

if __name__ == '__main__':
	main()