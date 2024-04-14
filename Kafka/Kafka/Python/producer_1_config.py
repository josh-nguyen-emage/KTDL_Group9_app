from confluent_kafka import Producer
import time
from datetime import datetime
import random
import json

# Configuration for your Kafka producer
config_1 = {
    'bootstrap.servers': 'localhost:9092', # Change this to your Kafka broker's address
    'client.id': 'Click-Bag' # Optional, but good to have for identifying your producer
}
# Topic you want to publish to
topic_1a = 'Click'
topic_1b = 'ShoppingBag'
producer_1a = Producer(**config_1)
producer_1b = Producer(**config_1)
# Function to deliver reports asynchronously
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')

# categories_length = 10
# categories_list = ['Túi xách và Vali túi du lịch', 'Giày dép & Quần áo nữ', 'TV & Video', 'Màn hình & Máy in', 'Điện thoại & Máy tính bảng', 'Electronics Accessories', 'Thiết bị thông minh', 'Máy ảnh & Máy bay camera', 'Âm thanh', 'Máy vi tính & Laptop']

# Producer 1: 
def producer1_running():
    """Producer 1 function"""
    while True:
        customerID_num = random.randint(1,10000)
        customerID = 'customers/' + str(customerID_num) + '-A'
        categoryID_num = random.randint(1,10)
        categoryID = 'categories/' + str(categoryID_num) + '-A'
        # random_category_item = random.choice(categories_list)
        random_clicked_list = [customerID, categoryID]
        random_item_number_json = json.dumps(random_clicked_list)

        random_send = random.randint(0,1)

        # Produce a message. Note that the value must be a string or bytes.
        if (random_send == 0):
            # random_category_item = random.choice(categories_list)

            producer_1a.produce(topic_1a, value=random_item_number_json, callback=delivery_report)
            # Wait up to 1 second for events. Callbacks will be invoked during
            # this method call if the message is acknowledged.
            producer_1a.poll(1)
            print(f"Sent data with userID {customerID} item {categoryID}: times to topic: {topic_1a}")
        else: 
            # random_category_item = random.choice(categories_list)
            # timestamp_ms = int(time.time() * 1000)
            # random_bagged_list = [timestamp_ms, random_category_item]
            # random_item_number_json = json.dumps(random_bagged_list)
            producer_1b.produce(topic_1b, value=random_item_number_json, callback=delivery_report)
            # Wait up to 1 second for events. Callbacks will be invoked during
            # this method call if the message is acknowledged.
            producer_1b.poll(1)
            print(f"Sent data with userID {customerID} item {categoryID}: times to topic: {topic_1b}")
        

        # Wait for 60 seconds before sending the next message
        random_second = random.randint(1,2)
        time.sleep(random_second)