# RC Rover

The goal of this project is to create an efficient H-bridge circuit that can be used for motor control in various scenarios. The H-bridge circuit is a crucial component in robotics, and this project aims to demonstrate its functionality by building a rover test platform. The primary objective is to design a circuit that allows the rover to move in different directions, such as forward, backward, left, and right, while maintaining stability and control.

The H-bridge circuit will have multiple applications in robotics and other industries, such as automotive and aerospace. It can be used to control motors in robots, drones, electric vehicles, and many other devices. By creating a robust and efficient H-bridge circuit, this project aims to contribute to the advancement of motor control technology.

The rover test platform will showcase the H-bridge circuit's capabilities in a real-world scenario. The platform will be able to traverse different terrains, navigate obstacles, and perform various maneuvers, demonstrating the circuit's stability and reliability. Overall, this project aims to provide a practical learning experience in motor control and robotics while contributing to the development of efficient motor control technology for various industries.

# Meeting 1:

Date: 03/12/23
Time: 9:15 - 12 PM

Reference Material: https://ecetechprojects.wordpress.com/2011/07/08/arduino-h-bridge-motor-control/

Finalized Proposal: https://1drv.ms/w/s!At5nmv7gLyVwkvE4l1jkQC4PCUBfSg?e=4K8k71

Discussed the H-Bridge Design and decided which parts would be used
  - Decided on using PNP and NPN transistors
  - 9V battery
  - DC motors
  
Sketched a simple reference circuit and built it for testing. While this circuit works, we found it to be lackluster in performance.
 
<img src="https://user-images.githubusercontent.com/69320369/224601874-c5b4059b-2ab1-4c97-a3c2-f3a50a5f6dbe.png" height="300" /> <img src="https://user-images.githubusercontent.com/77856636/234189781-3349c04d-6147-420b-950f-c7e52e6e4538.png" height="300" />

# Meeting 2:

Date: 03/18/23
Time: 2 - 8 PM

We made a simple schematic with transistors to understand the basics of how it would all work. We then decided to change the circuit to mosfets because VCC is higher than the gate voltages and because the mosfets have built-in reverse-bias diodes to help with overvoltage spikes when the car is braking. After we did that, we realized we still needed an NPN transistor to control the mosfets. The new circuit has 4 mosfets and 2 transistors. We used 10kohm pull-up resistors on the P-channel gates to latch them shut. According to our math this means we'll have ~0.1mA through the transistors. This will affect which resistor we put on the transistors bases. For now it's 2.2k but we might need to increase that a bit to 10k as well for less current on the base.

Using a 10k resistor  in series with the 2N2222 Collector, we will see around 1mA, assuming 10V from the battery. Using a 2.2k resistor in series with the 2N2222 Base, we see 1.4mA, assuming 3.0v from the Pi. Given these parameters, we will expect <0.1V from the collector to emitter, so the MOSFET Gates will be basically grounded when the respective PI pin is HIGH. Conversely, in order flip the MOSFET gates HIGH, current into the base will need to be <7nA. Assuming we're using the 2.2k resistor, the PI output pin must be at <0.0154V relative to ground. In the real world, this might prove difficult, and testing will be required.

<img src="https://user-images.githubusercontent.com/69320369/226380973-0f21aae3-170d-4731-864c-b7e31b808524.png" width="400" />

Updated TinkerCad:

<img src="https://user-images.githubusercontent.com/69320369/226380291-c77ee0eb-ffea-4c81-8b9d-a37d5abbd992.png" width="400" />

Parts List: https://1drv.ms/x/s!At5nmv7gLyVwkvcxxzeMtASVYCzkrQ?e=bIrlzk

# Meeting 3:

Date: 03/19/23
Time: 5 - 9 PM

Reference Material: https://datasheets.raspberrypi.com/rpi3/raspberry-pi-3-b-plus-reduced-schematics.pdf

We designed a simple chassis and printed it. As for the power system we are using a 9.6V 2000 mAh battery with a voltage regulator for the H bridge circuit and a voltage regulator to power the pi with 5V. The remaining parts were also bought. 

<img src="https://user-images.githubusercontent.com/77856636/234189938-992c598c-2133-4645-8375-caff0fbf6a8d.png" height="300" />

<img src="https://user-images.githubusercontent.com/69320369/226381850-392b5e93-d138-4c30-b5b8-187398b2b5b0.png" height="300" /> <img src="https://user-images.githubusercontent.com/69320369/231038959-d5fa641d-8114-4bde-9970-b276c4396e6b.jpg" height="300" />

# Meeting 4:

Date: 03/24/23
Time: 12-12:30 PM
 
We are waiting for the remaining parts to arrive in the mail. 1/4 motors is completely built and tested. All that is left is building the full circuit on the breadboard and running tests on it. We spoke to Dr.Wolfe and discussed possibly presenting our demo earlier than the proposed presentation date. 

<img src="https://media.discordapp.net/attachments/1070823721411018833/1088686438297641010/20230323_234908.jpg?width=312&height=555" height="300" /> <img src="https://media.discordapp.net/attachments/1070823721411018833/1088686791336407120/20230323_233629.jpg?width=312&height=553" height="300" />

# Meeting 5:

Date: 03/25/23
Time: 6-9 PM

Reference Material: https://github.com/besp9510/dma_pwm

We were choosing between running the motors with a constant DC source and changing the voltage in order to change the speed or using PWM. With DC we could only get down to 4 [V]. With PWM, it went as low as 1.5vRMS and was still turning, and it is much easier to code. We ran some tests on the circuit with a frequency generator to test the PWM and saw some 1 [A] spikes from each motor. We discussed adding a filter or switching the motors so they are staggered so that we don't blow a fuse in our circuit. 

<img src="https://media.discordapp.net/attachments/1070823721411018833/1088969448154738718/20230324_175527.jpg?width=987&height=555" height="200" />

An example of what we could do to stagger the motors:

<img src="https://media.discordapp.net/attachments/1070823721411018833/1089057688039727115/PWM20Stagger.png?width=706&height=405" height="200" />

We finished fully building the rover, the only thing remaining was adding all the connectors and the circuit.

<img src="https://media.discordapp.net/attachments/1070823721411018833/1089547193486155896/20230326_084949.jpg?width=312&height=553" height="300" /> <img src="https://media.discordapp.net/attachments/1070823721411018833/1089547193167380491/20230326_084758.jpg?width=312&height=553" height="300" /> <img src="https://user-images.githubusercontent.com/77856636/234190092-d907f687-08b4-4fab-9e03-6d91f0ebbbd6.png" height="300" /> 

We discussed which controller we would use to control the robot. We could connect an Xbox controller with analog thumb sticks using bluetooth or use a numpad with different numbers signalling different speeds. We need to work on the code so we can program the directions using the following table:
 
<img src="https://media.discordapp.net/attachments/1070823721411018833/1089817415908610108/image.png?width=535&height=555" height="300" /> 

We also finalized a simple schematic for how the switchboard will be wired up suppling VCC to the voltage regulator, RPI regulator and light

<img src="https://media.discordapp.net/attachments/1070823721411018833/1089819112106115112/rn_image_picker_lib_temp_2e97c4f8-33c7-49ef-ae3b-879236283686.jpg?width=312&height=553" height="300" />

Current version of the H-Bridge schematic:

<img src="https://user-images.githubusercontent.com/69320369/229191431-44b014b4-56c6-40b3-8c9d-de0a184eca29.png" height="250" /> <img src="https://user-images.githubusercontent.com/69320369/229191877-9a6d93dd-2410-4f10-ad3c-a063bb9ff0b6.png" height="250" />


# Meeting 6:

Date: 03/30/23
Time: 2:30 - 5 PM

Reference Material: https://learn.adafruit.com/improve-brushed-dc-motor-performance/pwm-and-brushed-dc-motors

Finalized Working TinkedCad Circuit: https://www.tinkercad.com/things/bnNonHPksck-fantastic-hillar/editel?sharecode=lQiAWzKQ8pHRZROjkhvst0w-F3ZCxrJRO_LkxZTcMJo

PWM Motor Calculations: https://1drv.ms/x/s!At5nmv7gLyVwkvc0S1sMwEzTU4Yw9A?e=w484rG

The rover circuit was built on a separate breadboard for testing and we got 1 wheel working. We will eventually build the circuit on the breadboard that is already attached to the rover. The flyback diode in the circuit and the mosfets fixed the spikes that appeared when using PWM. Most of the code was written and added to the github repository. 

<img src="https://user-images.githubusercontent.com/69320369/229192614-bd41dcf6-abbb-4d40-9a7c-6549bf6996ab.png" height="300" /> <img src="https://user-images.githubusercontent.com/69320369/230246072-87da07ba-cce4-4893-94e3-b1aad60b3247.png" height="300" />

Finalized circuit schematic:

<img src="https://user-images.githubusercontent.com/69320369/231345186-a358f26f-9370-4e3c-b76b-9513721ffc63.png" height="300">

# Meeting 7: 

Date: 04/08/23
Time: 4-6 PM

Reference Material: https://github.com/zeth/inputs

The circuit was fully built and tested. We had a small setbacks with a regulator breaking but a new one was ordered to replace the broken one. Currently the rover is being controlled by a keypad but we are working on converting that to a joystick so that it is easier to work with. 

<img src="https://user-images.githubusercontent.com/69320369/231039480-752c6867-cba8-47a5-9bc7-2bd0a43fa6b2.jpg" height="250" /> <img src="https://user-images.githubusercontent.com/69320369/231039562-1e474c47-5c0b-4fd5-be2c-2a3609dbfe30.jpg" height="250" /> <img src="https://user-images.githubusercontent.com/69320369/231039684-21ac4d0c-4525-42d3-a1df-28c67b8f256c.jpg" height="250" />

The joystick will output a rectangular coordinate which needs to be converted to polar coordinates. Polar coordinates are typically used for omniwheels because their direction is controlled through angles which can be more intuitively visualized through polar coordinates. We will then add 315 to the polar angle to get rid of the negative angles for when the rover moves backwards. Then we can use the function dif['angle'] %= 360 to convert to 0~360 degrees. Then take cos() and sin() to get speed for the wheels and multiply each speed by the polar magnitude. That will give us the PWM duty cycle for each wheel. If it's positive, it will be put on pins 13, 9, 25, and 20. If it's negative (the wheel is going backwards) so it will be put on the output pins 26, 11, 16 and 21.

<img src="https://user-images.githubusercontent.com/69320369/231041050-f257de92-3133-4c84-8cca-9db9b6177f1b.png" height="250" /> <img src="https://user-images.githubusercontent.com/69320369/231041153-f7301ce1-f353-4433-a3d4-9ea80fde29e1.png" height="250" /> 

# Final Images:

<img src="https://user-images.githubusercontent.com/77856636/234191453-c93bd1df-ba9f-4b9c-936c-8593f362584e.jpg" height="250" /> <img src="https://user-images.githubusercontent.com/77856636/234191554-d130412e-fa0e-4c0d-926e-94906ea2d6db.jpg" height="250" /> <img src="https://user-images.githubusercontent.com/77856636/234191921-90192d81-09ae-4225-bd04-4b99cedee0e2.jpg" height="250" /> 










