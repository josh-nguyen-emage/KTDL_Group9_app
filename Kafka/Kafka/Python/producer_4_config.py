from confluent_kafka import Producer
import time
import random
import json

# Configuration for your Kafka producer
config_4 = {
    'bootstrap.servers': 'localhost:9092', # Change this to your Kafka broker's address
    'client.id': 'ProductSold' # Optional, but good to have for identifying your producer
}
# Topic you want to publish to
topic_4 = 'ProductReview'

producer_4 = Producer(**config_4)

# Function to deliver reports asynchronously
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')

# Producer 4: 
def producer4_running():
    """Producer 4 function"""
    while True:
        
        productID_num = random.randint(1,1841)
        productID = 'products/' + str(productID_num) + '-A'
        reviewStarNumber = random.randint(1,5)

        random_item_number= [productID, reviewStarNumber]

        random_item_number_json = json.dumps(random_item_number)
        random_second = random.randint(1,2)

        # Produce a message. Note that the value must be a string or bytes.
        producer_4.produce(topic_4, value=random_item_number_json, callback=delivery_report)
        
        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        producer_4.poll(1)

        print(f"Sent data with productionID {productID}: reviewNumber {reviewStarNumber} to topic: {topic_4}")

        # Wait for 60 seconds before sending the next message
        time.sleep(random_second)