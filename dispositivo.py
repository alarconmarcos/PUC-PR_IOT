import paho.mqtt.client as mqtt
import time


usuario = ''
password = ''
client_id = 'xuxumelancia'
server = 'broker.mqttdashboard.com'
port = 1883


client = mqtt.Client(client_id)
client.username_pw_set(usuario, password)  
client.connect(server, port)

client.publish('pucpr/iotmc/alarcon/temperatura', '24.1')
time.sleep(1)
  

client.disconnect()