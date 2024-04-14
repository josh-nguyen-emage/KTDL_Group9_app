from confluent_kafka import Consumer, KafkaError
import time
import os
import threading
import RavenDBHelper

# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Topic to consume from
topic_2 = 'ProductSold'

# Consumer configuration
consumer_config_2 = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'group1',
    'auto.offset.reset': 'latest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer_2 = Consumer(consumer_config_2)

# Subscribe to the topic
consumer_2.subscribe([topic_2])

# Initialize a list to accumulate messages
accumulated_messages_2 = []

characters_to_remove = ['"', '[', ']']

filename_2 = '../listener-output-log/product_sold_last_minutes.txt'

# listener 2
def listener2_running():
    while True:
        
        start_time = time.time()
        while time.time() - start_time < 60:
            msg = consumer_2.poll(timeout=0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            raw_message = msg.value().decode('utf-8')
            accumulated_messages_2.append(raw_message)
            RavenDBHelper.update_product_sale(raw_message)
        
        # Print accumulated messages
        print("Message received last minutes at ProductSold is updated in product_sold_last_minutes.txt")

        
        with open(filename_2, 'w') as file:
            pass
        # # Consume messages for one minute

        with open(filename_2, 'a') as file:  
            file.write("Accumulated messages received in the last minute:\n ")
            file.write(str(time.time()) + '\n')
            for message in accumulated_messages_2:
                file.write((message) + '\n')

        # Read the contents of the file
        with open(filename_2, 'r') as file:
            file_contents = file.read()

        # Replace all occurrences of ', ' with '#'
        file_contents = file_contents.replace(', ', '#')

        # Remove all occurrences of '"', '[', and ']'
        for char in characters_to_remove:
            file_contents = file_contents.replace(char, '')

        # Write the modified contents back to the file
        with open(filename_2, 'w') as file:
            file.write(file_contents)

        # Clear the accumulated messages list for the next iteration
        accumulated_messages_2.clear()
        
        # Sleep for the remaining time until one minute has passed
        time.sleep(max(0, 60 - (time.time() - start_time)))

