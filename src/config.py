# Configuration shared between producer and consumer

# Connecting to your local Kafka on default port
BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC_NAME = 'user-email-updates'

# Common Producer configuration
PRODUCER_CONF = {
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'client.id': 'email-app-producer',
    # ensure idempotence (exactly-once)
    'enable.idempotence': True 
}

# Common Consumer configuration
CONSUMER_CONF = {
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': 'email-updates-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}
