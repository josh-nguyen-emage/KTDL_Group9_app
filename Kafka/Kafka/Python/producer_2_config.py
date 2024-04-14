from confluent_kafka import Producer
import time
import random
import json
from datetime import datetime

# Configuration for your Kafka producer
config_2 = {
    'bootstrap.servers': 'localhost:9092', # Change this to your Kafka broker's address
    'client.id': 'ProductSold' # Optional, but good to have for identifying your producer
}
# Topic you want to publish to
topic_2 = 'ProductSold'

producer_2 = Producer(**config_2)

# Function to deliver reports asynchronously
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')

# Producer 2: 
def producer2_running():
    """Producer 2 function"""
    while True:
        #random_categery_item = random.choice(categories_list)
        # random_item_number =  [random.randint(0, 10) for _ in range(categories_length)] #random the data bought by consumer
        productID_num = random.randint(1,1841)
        productID = 'products/' + str(productID_num) + '-A'
        numberSold = random.randint(1,10)
        transactionID_num = random.randint(100000,200000)
        transactionID = 'TID' + str(transactionID_num)
        
        # Get the current Unix timestamp
        unix_timestamp = time.time()

        # Convert the Unix timestamp to a datetime object
        datetime_obj = datetime.utcfromtimestamp(unix_timestamp)

        # Format the datetime object as a string in the desired format
        timestamp = datetime_obj.strftime('%Y-%m-%d')
        # timestamp = int(time.time() * 1000)


        random_item_number= [productID, transactionID, numberSold, timestamp]

        random_item_number_json = json.dumps(random_item_number)
        random_second = random.randint(1,2)

        # Produce a message. Note that the value must be a string or bytes.
        producer_2.produce(topic_2, value=random_item_number_json, callback=delivery_report)
        
        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        producer_2.poll(1)

        print(f"Sent data with ID{transactionID}: productID: {productID} to topic: {topic_2}")

        # Wait for 60 seconds before sending the next message
        time.sleep(random_second)