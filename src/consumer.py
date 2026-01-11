import json
from confluent_kafka import Consumer, KafkaException, KafkaError
from src.config import CONSUMER_CONF, TOPIC_NAME


def process_email_change(data):
    """
    Mock function to handle the business logic.
    E.g., Update database, send confirmation email, invalidate auth tokens.
    """
    u_id = data.get('user_id')
    email = data.get('new_email')
    print(f" -> ACTION: Updating system records for User {u_id} to {email}")


def main():
    consumer = Consumer(CONSUMER_CONF)
    consumer.subscribe([TOPIC_NAME])

    print(f"--- Consumer listening on '{TOPIC_NAME}' ---")

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            
            if msg is None: 
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            
            # Decode and process
            try:
                val = msg.value().decode('utf-8')
                data = json.loads(val)
                process_email_change(data)
                
                # Checkpointing: Commit offset only after successful processing
                consumer.commit(asynchronous=False)
                
            except Exception as e:
                print(f"Error processing message: {e}")

    except KeyboardInterrupt:
        print("\nStopping consumer...")
    finally:
        consumer.close()


if __name__ == '__main__':
    main()
