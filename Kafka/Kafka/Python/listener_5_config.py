from confluent_kafka import Consumer, KafkaError
import time
import os
import RavenDBHelper
import threading
# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Topic to consume from
topic_5 = 'SellerReview'

# Consumer configuration
consumer_config_5 = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'latest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer_5 = Consumer(consumer_config_5)

# Subscribe to the topic
consumer_5.subscribe([topic_5])

# Initialize a list to accumulate messages
accumulated_messages_5 = []

filename_5 = '../listener-output-log/seller_review.txt'

# listener 5
def listener5_running():
    while True:
        
        start_time = time.time()
        while time.time() - start_time < 60:
            msg = consumer_5.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            
            raw_message = msg.value().decode('utf-8')
            accumulated_messages_5.append(raw_message)
            RavenDBHelper.update_seller_review(raw_message)
        
        # Print accumulated messages
        print("Message received last minutes at SellerReview is updated in seller_review.txt")
       
        
        with open(filename_5, 'w') as file:
            pass
        # Consume messages for one minute

        with open(filename_5, 'a') as file:  
            file.write("Accumulated messages received in the last minute:\n ")
            file.write(str(time.time()) + '\n')
            for message in accumulated_messages_5:
                file.write((message) + '\n')

        # Read the contents of the file
        with open(filename_5, 'r') as file:
            file_contents = file.read()

        # Replace all occurrences of ', ' with '#'
        file_contents = file_contents.replace(', ', '#')

        # Remove all occurrences of '"', '[', and ']'
        characters_to_remove = ['"', '[', ']']
        for char in characters_to_remove:
            file_contents = file_contents.replace(char, '')

        # Write the modified contents back to the file
        with open(filename_5, 'w') as file:
            file.write(file_contents)

        # Clear the accumulated messages list for the next iteration
        accumulated_messages_5.clear()
        
        # Sleep for the remaining time until one minute has passed
        time.sleep(max(0, 60 - (time.time() - start_time)))