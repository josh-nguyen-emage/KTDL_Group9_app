from confluent_kafka import Consumer, KafkaError
import time
# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Topic to consume from
topic_6 = 'ProductSold'

# Consumer configuration
consumer_config_6 = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'group2',
    'auto.offset.reset': 'earliest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer_6 = Consumer(consumer_config_6)

# Subscribe to the topic
consumer_6.subscribe([topic_6])

# Initialize a list to accumulate messages
accumulated_messages_6 = []

filename_6 = '../listener-output-log/product_sold_all_times.txt'




# listener 6
def listener6_running():
    while True:
        
        start_time = time.time()
        while time.time() - start_time < 60:
            msg = consumer_6.poll(timeout=0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            accumulated_messages_6.append(msg.value().decode('utf-8'))
        
        # Print accumulated messages
        print("Message received all times at topic ProductSold is updated in product_sold_all_times.txt")

        with open(filename_6, 'a') as file:  
            for message in accumulated_messages_6:
                file.write((message) + '\n')

                # Read the contents of the file
        with open(filename_6, 'r') as file:
            file_contents = file.read()

        # Replace all occurrences of ', ' with '#'
        file_contents = file_contents.replace(', ', '#')

        # Remove all occurrences of '"', '[', and ']'
        characters_to_remove = ['"', '[', ']']
        for char in characters_to_remove:
            file_contents = file_contents.replace(char, '')

        # Write the modified contents back to the file
        with open(filename_6, 'w') as file:
            file.write(file_contents)

        # Clear the accumulated messages list for the next iteration
        accumulated_messages_6.clear()
        
        # Sleep for the remaining time until one minute has passed
        time.sleep(max(0, 60 - (time.time() - start_time)))




