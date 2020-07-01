# import pandas as pd
from time import sleep
import os
from kafka import KafkaProducer
from json import dumps

directory = os.getcwd()

# data = pd.read_csv(directory+'/Producer App/Scores.csv')

# print(data.head())

producer = KafkaProducer(bootstrap_servers = ['10.0.1.4:9094'],
                        value_serializer = lambda x:dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number':e}
    producer.send('multibroker',value=data)
    sleep(60)

# for values in range(5,data.shape[0],5):
#     print(data.iloc[values-5:values,:])
#     json_data = data.iloc[values-5:values,:].to_json(orient='index')
#     producer.send('commentary_data',value=json_data)
#     sleep(60)
