from time import sleep
from string import ascii_uppercase
from random import randint
import hashlib
from confluent_kafka import Producer
import socket
import json

conf = {"bootstrap.servers": "kafka:9092", "client.id": socket.gethostname()}
producer = Producer(conf)

while True: 
    category = ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
    level = randint(0,100)
    count = randint(0,3000)
    summ = round(randint(0,100000) + randint(0,1000) / 1500, 3)
    contragent = hashlib.md5(str(randint(0,1000) + 3).encode()).hexdigest()[:6]
    desc = hashlib.md5(str(randint(0,10000)).encode()).hexdigest() * 2
    msg = {
        "category": category,
        "level": level,
        "count": count,
        "summ": summ,
        "contragent": contragent,
        "desc": desc,
    }
    producer.produce("sales_in_game", value = json.dumps(msg))
    sleep(1)
