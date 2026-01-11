import json
import time
import random
from confluent_kafka import Producer
from src.config import PRODUCER_CONF, TOPIC_NAME


def delivery_callback(err, msg):
    """Called once for each message produced to indicate delivery result."""
    if err:
        print(f"ERROR: Message failed delivery: {err}")
    else:
        print(f"Produced event to {msg.topic()} key={msg.key().decode('utf-8')}")


def main():
    producer = Producer(PRODUCER_CONF)
    
    print(f"--- Producer started. Publishing to '{TOPIC_NAME}' ---")
    print("Press Ctrl+C to stop.")

    # List of fake user IDs to simulate
    user_ids = [101, 102, 103, 104, 105]

    try:
        while True:
            # Simulate a user action
            user_id = str(random.choice(user_ids))
            new_email = f"user{user_id}.{random.randint(1, 1000)}@example.com"
            
            event_data = {
                "event": "EMAIL_UPDATED",
                "user_id": user_id,
                "new_email": new_email,
                "timestamp": time.time()
            }

            key = user_id  # Important: Using ID as key guarantees order per user
            value = json.dumps(event_data)

            producer.produce(
                TOPIC_NAME, 
                key=key, 
                value=value, 
                callback=delivery_callback
            )
            
            # Poll ensures callbacks are handled
            producer.poll(0)
            
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping producer...")
    finally:
        # Wait for outstanding messages to be delivered
        producer.flush()


if __name__ == '__main__':
    main()
