
import RPi.GPIO as GPIO
import time

SENSOR_PIN = [14, 15]  # Replace with the actual GPIO pin numbers you're using
SAMPLE_TIME = 500  # Sampling time in milliseconds
SAMPLE_INTERVAL = 0.005  # Time interval for counting sound events in seconds

GPIO.setmode(GPIO.BCM)

for pin in SENSOR_PIN:
    GPIO.setup(pin, GPIO.IN)

output_values = [0, 0]


def map_value(value):
    # Ensure the input value is within the specified range
    if value < 0:
        value = 0
    elif value > 640:
        value = 640
    
    # Calculate the mapped value
    # mapped_value = (value - min_input) * (max_output - min_output) / (max_input - min_input) + min_output
    mapped_value = (value)*(140-10)/(640)+10
    return mapped_value

def count_sound_events(pin, interval):
    count = 0
    start_time = time.time()

    while time.time() - start_time <= interval:
        if GPIO.input(pin) == GPIO.LOW:
            count += 1

    return count

def calculate_sound_intensity():
    while True:
        sound_events = [count_sound_events(pin, SAMPLE_INTERVAL) for pin in SENSOR_PIN]

        # You can directly use the count of sound events as the intensity
        mapped_events = [map_value(sound_events[i]) for i in range(0,1,1)]
        output_values = mapped_events
        print(f"Sound Intensity list: {output_values} events")

        time.sleep(SAMPLE_TIME / 1000.0)

try:
    calculate_sound_intensity()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()