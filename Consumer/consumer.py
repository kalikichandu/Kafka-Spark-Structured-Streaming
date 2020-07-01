from time import sleep
import os
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'multibroker',
     bootstrap_servers=['10.0.1.4:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     #group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('{}'.format(message))
