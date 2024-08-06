from time import sleep
from random import randint
import hashlib
from confluent_kafka import Producer
import socket
import json

conf = {"bootstrap.servers": "kafka:9092", "client.id": socket.gethostname()}
producer = Producer(conf)

while True: 
    r_int = randint(0,1000)
    r_string = hashlib.md5(str(r_int).encode()).hexdigest()
    r_string_small = hashlib.md5(str(r_int + 3).encode()).hexdigest()[:5]
    r_float = r_int / 1500
    msg = {
        "r_int" : r_int,
        "r_string" : r_string,
        "r_string_small" : r_string_small,
        "r_float" : r_float,
    }
    producer.produce("test_topic", value = json.dumps(msg))
    sleep(1)
