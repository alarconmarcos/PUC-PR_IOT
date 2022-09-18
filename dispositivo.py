import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import usuario, password, client_id, server, port


def mensagem(client, user, msg):
    vetor = msg.payload.decode().split(',')
    aquecedor('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{usuario}/things/{client_id}/response', f'ok,{vetor[0]}')

# Conexão inicial
client = mqtt.Client(client_id)
client.username_pw_set(usuario, password)  
client.connect(server, port)

client.on_message = mensagem
client.subscribe(f'v1/{usuario}/things/{client_id}/cmd/2')
client.loop_start()

# Comportamento do sistema
while True:
    client.publish(f'v1/{usuario}/things/{client_id}/data/0', temperatura())
    client.publish(f'v1/{usuario}/things/{client_id}/data/1', umidade())
    time.sleep(10)
  
# client.disconnect()