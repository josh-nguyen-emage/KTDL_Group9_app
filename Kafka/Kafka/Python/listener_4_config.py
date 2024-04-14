from confluent_kafka import Consumer, KafkaError
import time
import os
import threading
import RavenDBHelper
# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Topic to consume from
topic_4 = 'ProductReview'

# Consumer configuration
consumer_config_4 = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'latest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer_4 = Consumer(consumer_config_4)

# Subscribe to the topic
consumer_4.subscribe([topic_4])

# Initialize a list to accumulate messages
accumulated_messages_4 = []

filename_4 = '../listener-output-log/product_review.txt'

characters_to_remove = ['"', '[', ']']

# listener 4
def listener4_running():
    while True:
        
        start_time = time.time()
        while time.time() - start_time < 60:
            msg = consumer_4.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
                
            message_str = msg.value().decode('utf-8')
            accumulated_messages_4.append(message_str)
            RavenDBHelper.update_product_review(message_str)
        
        # Print accumulated messages
        print("Message received last minutes at ProductReview is updated in product_review.txt")
        
        with open(filename_4, 'w') as file:
            pass
        # Consume messages for one minute

        with open(filename_4, 'a') as file:  
            file.write("Accumulated messages received in the last minute:\n ")
            file.write(str(time.time()) + '\n')
            for message in accumulated_messages_4:
                file.write((message) + '\n')

                # Read the contents of the file
        with open(filename_4, 'r') as file:
            file_contents = file.read()

        # Replace all occurrences of ', ' with '#'
        file_contents = file_contents.replace(', ', '#')

        # Remove all occurrences of '"', '[', and ']'
        for char in characters_to_remove:
            file_contents = file_contents.replace(char, '')

        # Write the modified contents back to the file
        with open(filename_4, 'w') as file:
            file.write(file_contents)

        # Clear the accumulated messages list for the next iteration
        accumulated_messages_4.clear()
        
        # Sleep for the remaining time until one minute has passed
        time.sleep(max(0, 60 - (time.time() - start_time)))