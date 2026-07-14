import config

print("Kafka Server :", config.KAFKA_BOOTSTRAP_SERVERS)
print("Kafka Topic  :", config.KAFKA_TOPIC)
print("Events/sec   :", config.EVENTS_PER_SECOND)
print("Fraud %      :", config.FRAUD_PERCENTAGE)
print("Log Level    :", config.LOG_LEVEL)