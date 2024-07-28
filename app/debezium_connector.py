import requests
connector_name = "inventory-connector"

connection = {
  "name": connector_name,
  "config": {
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "tasks.max": "1",
    "database.hostname": "mysql",
    "database.port": "3306",
    "database.user": "mysqluser",
    "database.password": "mysqlpw",
    "database.server.id": "223344",
    "database.server.name": "dbserver",
    "topic.prefix": "dbserver",
    "database.history.kafka.bootstrap.servers": "kafka:9092",
    "database.history.kafka.topic": "schema-changes.inventory",
    "database.include.list": "inventory",
    "table.include.list": "inventory.orders",
    "database.history.internal.kafka.bootstrap.servers": "kafka:9092",
    "schema.history.internal.kafka.topic": "schema-changes.inventory-internal",

  }
}

print("send connector")

response = requests.delete(url=f'http://localhost:8083/connectors/{connector_name}')

result = requests.post(url='http://localhost:8083/connectors/', json=connection)
print(result.json())
