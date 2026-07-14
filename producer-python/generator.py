from fraud import inject_fraud
import random
import uuid
from faker import Faker
from datetime import datetime
fake=Faker();



EVENT_TYPES=[
  "USER_CREATED",
  "USER_LOGIN",
  "ORDER_PLACED",
  "PAYMENT_SUCCESS",
  "PAYMENT_FAILED",
  "COUPON_REQUESTED",
  "PASSWORD_RESET",
  "ADDRESS_UPDATED",
  "EMAIL_VERIFIED",
]

PAYMENT_METHODS=[
  "CARD",
  "UPI",
  "NETBANKING",
  "WALLET",
]

CURRENCIES=[
  "USED",
  "INR",
]

STATUSES=[
  "SUCCESS",
  "FAILED", 
  "PENDING"
]

def random_id(prefix:str)->str:
  return f"{prefix}_{uuid.uuid4().hex[:8]}"

def generate_event()-> dict:
  event_type=random.choice(EVENT_TYPES)
  event={
    "event_id": random_id("event"),
    "event_type": event_type,
    "timestamp": datetime.utcnow().isoformat(),

     "user_id": random_id("user"),
     "device_id": random_id("device"),
     "merchant_id": random_id("merchant"),
     "order_id": random_id("order"),
     "payment_id": random_id("payment"),
     "amount": round(random.uniform(10.0, 1000.0), 2),
     "currency": random.choice(CURRENCIES),
     "country": fake.country(),
     "city": fake.city(),
     "ip_address": fake.ipv4(),
     "payment_method": random.choice(PAYMENT_METHODS),
     "coupon_code":random.choice([None,"sAVE10","FREESHIP","WELCOME"]),
     "status": random.choice(STATUSES),
  }
  return inject_fraud(event)

if __name__=="__main__":
  for _ in range(5):
    print(generate_event())