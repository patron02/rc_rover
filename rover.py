import tkinter as tk
import RPi.GPIO as gpio

# Motor Connections on Pi
# motor M1: pins 20 and 21  (Back Right)
# motor M2: pins 13 and 26  (Back Left)
# motor M3: pins 25 and 16   (Front Right)
# motor M4: pins 9 and 11   (Front Left)

# Define pin mapping using a dictionary
pin_mapping = {
    'w': [9, 13, 20, 25],  # Forward \
    's': [11, 16, 21, 26],  # Back \
    'a': [11, 13, 21, 25],  # Left \
    'd': [9, 16, 20, 26],  # Right \
    
    'e': [9, 20],  # Forward Right \
    'z': [11, 21],  # Back Left \
    'q': [13, 25],  # Forward Left \
    'c': [16, 26],  # Back Right \
    
    ']': [9, 13, 16, 21],  # Rotate Right \
    '[': [11, 20, 25, 26],  # Rotate Left \
}

# Setup pins as outputs
gpio.setmode(gpio.BCM)
for pins in pin_mapping.values():
    for pin in pins:
        gpio.setup(pin, gpio.OUT) #defines all listed pins as Outputs
        gpio.output(pin, gpio.LOW) #set all pins LOW by default

pin = [] # initialize pin variable

def press_key(event):
    global pin # use the global pin variable
    key = event.char.lower() # get the pressed key in lowercase
    pin = pin_mapping.get(key, []) # get the corresponding pins for the key
    for p in pin:
        gpio.output(p, gpio.HIGH) # set each pin high

def release_key(event):
    global pin # use the global pin variable
    for p in pin:
        gpio.output(p, gpio.LOW) # set each pin low

root = tk.Tk()
root.bind('<KeyPress>', press_key)
root.bind('<KeyRelease>', release_key)
root.mainloop()

gpio.cleanup()
