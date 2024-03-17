#only to learn something about time library
# i got it, this code returns time difference between two events

import time

current_time_seconds = time.time()
print("starting time: ", current_time_seconds)
time.sleep(2)
end_time_seconds = time.time()
print("end time: ",end_time_seconds)
print("time difference: ",((end_time_seconds)-(current_time_seconds)))