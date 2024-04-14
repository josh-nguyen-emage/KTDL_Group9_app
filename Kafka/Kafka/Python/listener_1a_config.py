from confluent_kafka import Consumer, KafkaError
import time
import RavenDBHelper
# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Topic to consume from
topic_1a = 'ShoppingBag'

# Consumer configuration
consumer_config_1a = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'group1a',
    'auto.offset.reset': 'earliest'  # Start consuming from the latest offset
}

# Create Consumer instance
consumer_1a = Consumer(consumer_config_1a)

# Subscribe to the topic
consumer_1a.subscribe([topic_1a])

# Initialize a list to accumulate messages
accumulated_messages_1a = []

filename_1a = '../Python/other_txt/click.txt'




# listener 1a
def listener1a_running():
    while True:
        
        start_time = time.time()
        while time.time() - start_time < 60:
            msg = consumer_1a.poll(timeout=0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            raw_message = msg.value().decode('utf-8')
            accumulated_messages_1a.append(raw_message)
            RavenDBHelper.update_customer_recent_interested(raw_message)
        
        # Print accumulated messages
        print("Message received all times at topic Click is updated in click.txt")

        with open(filename_1a, 'a') as file:  
            for message in accumulated_messages_1a:
                file.write((message) + '\n')

                # Read the contents of the file
        with open(filename_1a, 'r') as file:
            file_contents = file.read()

        # Replace all occurrences of ', ' with '#'
        file_contents = file_contents.replace(', ', '#')

        # Remove all occurrences of '"', '[', and ']'
        characters_to_remove = ['"', '[', ']']
        for char in characters_to_remove:
            file_contents = file_contents.replace(char, '')

        # Write the modified contents back to the file
        with open(filename_1a, 'w') as file:
            file.write(file_contents)

        # Clear the accumulated messages list for the next iteration
        accumulated_messages_1a.clear()
        
        # Sleep for the remaining time until one minute has passed
        time.sleep(max(0, 60 - (time.time() - start_time)))