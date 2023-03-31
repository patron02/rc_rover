import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

# Set default PWM settings
frequency = 1500    # Hz
duty_cycle = 0.75   # 75%

# Define pin mapping using a dictionary
pin_mapping = {
    'w': [7, 11, 15, 21],  # Forward \
    's': [8, 12, 16, 22, 33],  # Back \
    'a': [8, 11, 15, 22],  # Left \
    'd': [7, 12, 16, 21],  # Right \

    'e': [7, 21],  # Forward Right \
    'z': [8, 22, 33],  # Back Left \
    'q': [11, 15],  # Forward Left \
    'c': [12, 16, 33],  # Back Right \
    
    ']': [8, 11, 16, 21],  # Rotate Right \
    '[': [7, 12, 15, 22],  # Rotate Left \
}

# Setup pins as outputs
for pins in pin_mapping.values():
    for pin in pins:
        gpio.setup(pin, gpio.OUT) #defines all listed pins as Outputs

# Define key change duty cycle callback function
def key_change_dc(key):
    global duty_cycle
    if key.isdigit():
        num = int(key)
        if num == 0:
            duty_cycle = 1.0
        else:
            duty_cycle = num / 10.0
            
# Define key press callback function
def key_press(key):
    global duty_cycle
    pins = pin_mapping.get(key) #assign pins per key press
    if pins:
        for pin in pins:
            pwm = gpio.PWM(pin, frequency)
            pwm.start(duty_cycle) #sets pins to PWM

# Define key release callback function
def key_release(key):
    pins = pin_mapping.get(key) #assign pins per key release
    if pins:
        for pin in pins:
            pwm = gpio.PWM(pin, frequency)
            pwm.stop() #sets pins to LO

try:
    while True:
        key = input("Press a WSAD key: ")
        if not any(key in keys for keys in pin_mapping.keys()):
            key_change_dc(key)
            debounced_key_press = debounce(key_press)
            debounced_key_release = debounce(key_release)
        if key in valid_keys:
            debounced_key_press(key)
            time.sleep(0.1)
            debounced_key_release(key)
        else:
            print("Invalid key!")

except KeyboardInterrupt:
    gpio.cleanup()
