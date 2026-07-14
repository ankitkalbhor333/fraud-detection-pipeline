import os
import time
from kafka import KafkaProducer, errors

bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
topic = os.getenv("KAFKA_TOPIC", "fraud-events")


def create_producer():
    return KafkaProducer(
        bootstrap_servers=[bootstrap_servers],
        value_serializer=lambda v: v.encode("utf-8"),
        request_timeout_ms=10000,
    )


producer = None
while producer is None:
    try:
        producer = create_producer()
        print(f"Connected to Kafka at {bootstrap_servers}")
    except errors.NoBrokersAvailable as exc:
        print(f"Kafka not ready yet: {exc}. Retrying in 5 seconds...")
        time.sleep(5)

while True:
    try:
        message = f"fraud-event-{int(time.time())}"
        producer.send(topic, message)
        producer.flush()
        print(f"Sent: {message}")
        time.sleep(2)
    except errors.KafkaError as exc:
        print(f"Kafka send failed: {exc}. Reconnecting...")
        producer = None
        while producer is None:
            try:
                producer = create_producer()
                print(f"Reconnected to Kafka at {bootstrap_servers}")
            except errors.NoBrokersAvailable as retry_exc:
                print(f"Kafka still unavailable: {retry_exc}. Retrying in 5 seconds...")
                time.sleep(5)
