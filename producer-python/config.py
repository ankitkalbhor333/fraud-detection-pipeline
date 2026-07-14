import os 
from dotenv import load_dotenv;

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "fraud-events")
EVENTS_PER_SECOND = int(os.getenv("EVENTS_PER_SECOND", "5"))
FRAUD_PERCENTAGE = int(os.getenv("FRAUD_PERCENTAGE", "10"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")