import threading
import os
import listener_1a_config
import listener_1b_config
import listener_2_config
import listener_4_config
import listener_5_config
import listener_6_config
import Readfile

# Clean files before running
# filenamea = '../listener-output-log/product_sold_all_times.txt'
# if os.path.getsize(filenamea) > 0:
#             open(filenamea, 'w').close()  # Truncate the file
# filenameb = '../Python/other_txt/click.txt'
# if os.path.getsize(filenameb) > 0:
#             open(filenameb, 'w').close()  # Truncate the file
# filenamec = '../Python/other_txt/shopping_bag.txt'
# if os.path.getsize(filenamec) > 0:
#             open(filenamec, 'w').close()  # Truncate the file            

print('Start listening to all topic, the result will be generate in /listener-output-log dicrectory')
thread1a = threading.Thread(target=listener_1a_config.listener1a_running)
thread1b = threading.Thread(target=listener_1b_config.listener1b_running)
thread2 = threading.Thread(target=listener_2_config.listener2_running)
thread4 = threading.Thread(target=listener_4_config.listener4_running)
thread5 = threading.Thread(target=listener_5_config.listener5_running)
thread6 = threading.Thread(target=listener_6_config.listener6_running)
thread7 = threading.Thread(target=Readfile.Readfile_running)
# Main loop to read and accumulate data every one minute
try:
    thread1a.start()
    thread1b.start()
    thread2.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()

    thread1a.join()
    thread1b.join()
    thread2.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()

except KeyboardInterrupt:
    pass
finally:
    listener_1a_config.consumer_1a.close()
    listener_1b_config.consumer_1b.close()
    listener_2_config.consumer_2.close()
    listener_4_config.consumer_4.close()
    listener_5_config.consumer_5.close()
    listener_6_config.consumer_6.close()