import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import usuario, password, client_id, server, port

# Conexão inicial
client = mqtt.Client(client_id)
client.username_pw_set(usuario, password)  
client.connect(server, port)

# Comportamento do sistema
while True:
    client.publish('pucpr/iotmc/alarcon/temperatura', temperatura())
    client.publish('pucpr/iotmc/alarcon/umidade', umidade())
    time.sleep(5)
  
# client.disconnect()