import paho.mqtt.publish as publish

publish.single("paho/test/single", "bgst lu hong", hostname="localhost")
