import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor

usuario = ''
password = ''
client_id = 'xuxumelancia'
server = 'broker.mqttdashboard.com'
port = 1883

client = mqtt.Client(client_id)
client.username_pw_set(usuario, password)  
client.connect(server, port)

while True:
    client.publish('pucpr/iotmc/alarcon/temperatura', temperatura())
    client.publish('pucpr/iotmc/alarcon/umidade', umidade())
    time.sleep(1)
  
# client.disconnect()