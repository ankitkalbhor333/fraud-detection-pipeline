
import time
import logging

import config
from generator import generate_event
from producer import EventProducer

logging.basicConfig(
    level=config.LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    producer = EventProducer()

    logger.info("========================================")
    logger.info(" Fraud Event Generator Started")
    logger.info(" Kafka Topic : %s", config.KAFKA_TOPIC)
    logger.info(" Events/sec  : %d", config.EVENTS_PER_SECOND)
    logger.info("========================================")

    try:
        while True:
            event = generate_event()

            producer.publish(event)

            time.sleep(1 / config.EVENTS_PER_SECOND)

    except KeyboardInterrupt:
        logger.info("Stopping producer...")

    finally:
        producer.close()
        logger.info("Producer stopped successfully.")


if __name__ == "__main__":
    main()
