from confluent_kafka import Producer
import threading
import producer_1_config
import producer_2_config
import producer_4_config
import producer_5_config






# Function to deliver reports asynchronously
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

#start thread
thread1 = threading.Thread(target=producer_1_config.producer1_running)
thread2 = threading.Thread(target=producer_2_config.producer2_running)
thread4 = threading.Thread(target=producer_4_config.producer4_running)
thread5 = threading.Thread(target=producer_5_config.producer5_running)


        
try:
    thread1.start()
    thread2.start()
    thread4.start()
    thread5.start()
    

    thread1.join()
    thread2.join()
    thread4.join()
    thread5.join()
except KeyboardInterrupt:
    print("Stopped.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait for any outstanding messages to be delivered and report failures
    producer_1_config.producer_1.flush()
    producer_2_config.producer_2.flush()
    producer_4_config.producer_4.flush()
    producer_5_config.producer_5.flush()

