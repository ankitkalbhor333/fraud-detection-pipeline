import json
import logging
from kafka import KafkaProducer
import config

logging.basicConfig(level=config.LOG_LEVEL,
                    format=
                    "%(asctime)s | %(levelname)s | %(message)s",)
logger = logging.getLogger(__name__)
class EventProducer:
  def __init__(self):
    self.producer=KafkaProducer(
      bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
      value_serializer=lambda v: json.dumps(v).encode("utf-8"),
      request_timeout_ms=10000,
      retries=5,
      acks="all",
    )

    logger.info(f"Connected to Kafka at {config.KAFKA_BOOTSTRAP_SERVERS}")

  def publish(self,event):
      """publish event to kafka topic"""
      future=self.producer.send(config.KAFKA_TOPIC, value=event)

      metadata=future.get(timeout=10)
      logger.info( "Published | topic=%s partition=%s offset=%s event=%s user=%s amount=%.2f", metadata.topic, metadata.partition, metadata.offset, event["event_type"], event["user_id"], event["amount"], )

  def close(self):
    self.producer.flush()
    self.producer.close()
      