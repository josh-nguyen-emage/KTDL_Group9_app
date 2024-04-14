from confluent_kafka import Consumer, KafkaError
import time
import RavenDBHelper
# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Topic to consume from
topic_1b = 'ShoppingBag'

# Consumer configuration
consumer_config_1b = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'group1b',
    'auto.offset.reset': 'earliest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer_1b = Consumer(consumer_config_1b)

# Subscribe to the topic
consumer_1b.subscribe([topic_1b])

# Initialize a list to accumulate messages
accumulated_messages_1b = []

filename_1b = '../Python/other_txt/shopping_bag.txt'




# listener 1b
def listener1b_running():
    while True:
        
        start_time = time.time()
        while time.time() - start_time < 60:
            msg = consumer_1b.poll(timeout=0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            raw_message = msg.value().decode('utf-8')
            accumulated_messages_1b.append(raw_message)
            RavenDBHelper.update_customer_recent_interested(raw_message)
        
        # Print accumulated messages
        print("Message received all times at topic ShoppingBag is updated in shopping_bag.txt")

        with open(filename_1b, 'a') as file:  
            for message in accumulated_messages_1b:
                file.write((message) + '\n')

                # Read the contents of the file
        with open(filename_1b, 'r') as file:
            file_contents = file.read()

        # Replace all occurrences of ', ' with '#'
        file_contents = file_contents.replace(', ', '#')

        # Remove all occurrences of '"', '[', and ']'
        characters_to_remove = ['"', '[', ']']
        for char in characters_to_remove:
            file_contents = file_contents.replace(char, '')

        # Write the modified contents back to the file
        with open(filename_1b, 'w') as file:
            file.write(file_contents)

        # Clear the accumulated messages list for the next iteration
        accumulated_messages_1b.clear()
        
        # Sleep for the remaining time until one minute has passed
        time.sleep(max(0, 60 - (time.time() - start_time)))




