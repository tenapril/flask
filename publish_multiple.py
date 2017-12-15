import paho.mqtt.publish as publish

msgs = [{'topic': "inTopic", 'payload': "multiple 1"}, ("inTopic", "multiple 2", 0, False), ("inTopic", "multiple asu", 0, False)]
publish.multiple(msgs, hostname="mau.nyalainlampu.ga", port=8883, auth={'username':"testuser",'password':"testpassword"})
