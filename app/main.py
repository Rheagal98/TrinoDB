from kafka import KafkaConsumer
import json
topic = "dbserver.inventory.orders"
consumer = KafkaConsumer(topic,
                         bootstrap_servers=['localhost:9092'],
                        # api_version=(7, 3, 2),
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                         group_id='2_2',
                         value_deserializer=lambda x: x.decode('utf-8'),
                         consumer_timeout_ms=10000)

# consumer.subscribe([topic])

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
