# import RPi.GPIO as GPIO
# import time

# SENSOR_PIN = [14, 15]  # Replace with the actual GPIO pin numbers you're using
# SAMPLE_TIME = 500  # Sampling time in milliseconds
# SAMPLE_INTERVAL = 0.005  # Time interval for counting sound events in seconds

# GPIO.setmode(GPIO.BCM)

# for pin in SENSOR_PIN:
#     GPIO.setup(pin, GPIO.IN)

# output_values = [0, 0]


# def map_value(value):
#     # Ensure the input value is within the specified range
#     if value < 1:
#         value = 1
#     elif value > 640:
#         value = 640
    
#     # Calculate the mapped value
#     mapped_value = (value)*(130)/(650)
#     return mapped_value

# def count_sound_events(pin, interval):
#     count = 0
#     start_time = time.time()

#     while time.time() - start_time <= interval:
#         if GPIO.input(pin) == GPIO.LOW:
#             count += 1
#     val=map_value(count)
#     return val

# def calculate_sound_intensity():
#     while True:
#         sound_events = [count_sound_events(pin, SAMPLE_INTERVAL) for pin in SENSOR_PIN]

#         # You can directly use the count of sound events as the intensity
#         #mapped_events = [map_value(sound_events[i]) for i in range(0,1,1)]
#         output_values = sound_events
#         print(f"Sound Intensity list: {output_values} events")

#         time.sleep(SAMPLE_TIME / 1000.0)

# try:
#     calculate_sound_intensity()

# except KeyboardInterrupt:
#     pass

# finally:
#     GPIO.cleanup()




# *****************************************

# for six sensor


# import RPi.GPIO as GPIO
# import time

# SENSOR_PIN = [14, 15 ,18, 23, 24, 25]  # Replace with the actual GPIO pin numbers you're using
# SAMPLE_TIME = 500  # Sampling time in milliseconds
# SAMPLE_INTERVAL = 0.005  # Time interval for counting sound events in seconds

# GPIO.setmode(GPIO.BCM)

# for pin in SENSOR_PIN:
#     GPIO.setup(pin, GPIO.IN)

# output_values = [0,0,0,0,0,0]


# def map_value(value):
#     # Ensure the input value is within the specified range
#     if value < 1:
#         value = 1
#     elif value > 640:
#         value = 640
    
#     # Calculate the mapped value
#     mapped_value = (value)*(130)/(650)
#     return mapped_value

# def count_sound_events(pin, interval):
#     count = 0
#     start_time = time.time()

#     while time.time() - start_time <= interval:
#         if GPIO.input(pin) == GPIO.LOW:
#             count += 1
#     val=map_value(count)
#     return val

# def calculate_sound_intensity():
#     while True:
#         sound_events = [count_sound_events(pin, SAMPLE_INTERVAL) for pin in SENSOR_PIN]

#         # You can directly use the count of sound events as the intensity
#         #mapped_events = [map_value(sound_events[i]) for i in range(0,1,1)]
#         output_values = sound_events
#         print(f"Sound Intensity list: {output_values} events")

#         time.sleep(SAMPLE_TIME / 1000.0)

# try:
#     calculate_sound_intensity()

# except KeyboardInterrupt:
#     pass

# finally:
#     GPIO.cleanup()


# *************************************

# final integration


import RPi.GPIO as GPIO
import time

SENSOR_PIN = [14, 15 ,18, 23, 24, 25]  # Replace with the actual GPIO pin numbers you're using
SAMPLE_TIME = 500  # Sampling time in milliseconds
SAMPLE_INTERVAL = 0.005  # Time interval for counting sound events in seconds

GPIO.setmode(GPIO.BCM)

for pin in SENSOR_PIN:
    GPIO.setup(pin, GPIO.IN)

output_values = [0,0,0,0,0,0]


def map_value(value):
    # Ensure the input value is within the specified range
    if value < 1:
        value = 1
    elif value > 640:
        value = 640
    
    # Calculate the mapped value
    mapped_value = (value)*(130)/(650)
    return mapped_value

def count_sound_events(pin, interval):
    count = 0
    start_time = time.time()

    while time.time() - start_time <= interval:
        if GPIO.input(pin) == GPIO.LOW:
            count += 1
    val=map_value(count)
    return val

def calculate_sound_intensity():
    while True:
        sound_events = [count_sound_events(pin, SAMPLE_INTERVAL) for pin in SENSOR_PIN]
        output_values = sound_events
        print(f"Sound Intensity list: {output_values} events")
        f=open("data.txt","a")
        f.writelines(str(output_values)+'\n')
        f.close()
        time.sleep(SAMPLE_TIME / 1000.0)
try:
    calculate_sound_intensity()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()