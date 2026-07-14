import random
import  config

SHARED_DEVICES=[f"DEV_SHARED_{i}" for i in range(1,6)]
SHARED_IPS=[
  "203.0.113.10",
  "203.0.113.20",
  "198.51.100.15",
]

COUPONS=[
  "SAVE50",
  "SUPER80",
  "MEGA20",
]

def inject_fraud(event:dict)->dict:
  if random.randint(1,100)>config.FRAUD_PERCENTAGE:

    event["IS_FRAUD"]=False
    event["fraud_type"]=None
    return event
  
  fraud_type=random.choice([
    "HIGH_AMOUNT",
    "SHARED_DEVICE",
    "SHARED_IP",
    "MULTIPLE_COUPONS",
    "FAILED_PAYMENT",
    "COUPON_ABUSE",
  ])

  event["IS_FRAUD"]=True
  event["fraud_type"]=fraud_type

  if fraud_type=="HIGH_AMOUNT":
    event["amount"]=round(random.uniform(1000.0, 5000.0),2)
  if fraud_type=="SHARED_DEVICE":
    event["device_id"]=random.choice(SHARED_DEVICES)
  if fraud_type=="SHARED_IP":
    event["ip_address"]=random.choice(SHARED_IPS)
  if fraud_type=="MULTIPLE_COUPONS":
    event["coupon_code"]=random.choice(COUPONS)
  if fraud_type=="FAILED_PAYMENT":
    event["event_type"]="PAYMENT_FAILED"
    event["status"]="FAILED"
  if fraud_type=="COUPON_ABUSE":
    event["coupon_code"]=random.choice(COUPONS)
  return event