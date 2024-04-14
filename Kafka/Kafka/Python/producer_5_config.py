from confluent_kafka import Producer
import time
import random
import json

# Configuration for your Kafka producer
config_5 = {
    'bootstrap.servers': 'localhost:9092', # Change this to your Kafka broker's address
    'client.id': 'Product_Review' # Optional, but good to have for identifying your producer
}
# Topic you want to publish to
topic_5 = 'SellerReview'

producer_5 = Producer(**config_5)

# Function to deliver reports asynchronously
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')

# Producer 5: 
def producer5_running():
    """Producer 5 function"""
    while True:
        #Seller RANDOM from 1 to 500
        sellerID_num = random.randint(1,593)
        sellerID = 'sellers/' + str(sellerID_num) + '-A'
        reviewRating = random.randint(50,100)
        reviewResponseRate = random.randint(50,100)
        reviewShipOnline = random.randint(50,100)
        random_item_number= [sellerID, reviewRating, reviewResponseRate, reviewShipOnline]

        random_item_number_json = json.dumps(random_item_number)
        random_second = random.randint(1,2)

        # Produce a message. Note that the value must be a string or bytes.
        producer_5.produce(topic_5, value=random_item_number_json, callback=delivery_report)
        
        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        producer_5.poll(1)

        print(f"Sent data with sellerID {sellerID} to topic: {topic_5}")

        # Wait for 60 seconds before sending the next message
        time.sleep(random_second)