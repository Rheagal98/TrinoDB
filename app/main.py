from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                         group_id='1',
                         value_deserializer=lambda x: x.decode('utf-8'))
consumer.subscribe(['dbserver1.inventory.orders'])
topics = consumer.topics()
print(topics)
print(vars(consumer))

try:
    for message in consumer:
        print(f"Received message: ")
        data = json.loads(message.value)
        print('Before: ')
        print(data.get('payload').get('before'))
        print('After: ')
        print(data.get('payload').get('after'))
        consumer.commit()
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    consumer.close()