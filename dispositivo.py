import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import usuario, password, client_id, server, port


def mensagem(client, user, msg):
    if msg.topic == 'pucpr/iotmc/alarcon/aquecedor':
        aquecedor(msg.payload.decode())

# Conexão inicial
client = mqtt.Client(client_id)
client.username_pw_set(usuario, password)  
client.connect(server, port)

client.on_message = mensagem
client.subscribe('pucpr/iotmc/alarcon/aquecedor')
client.loop_start()

# Comportamento do sistema
while True:
    client.publish('pucpr/iotmc/alarcon/temperatura', temperatura())
    client.publish('pucpr/iotmc/alarcon/umidade', umidade())
    time.sleep(5)
  
# client.disconnect()