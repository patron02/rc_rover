# RC Rover

The goal of this project is to design and prototype an RC rover that can move in all directions to explore terrain. A rover is used to collect information and samples from a specific terrain. They are used by lots of companies, especially those focused on space or deep-sea exploration. Some specifications that we might need to consider are: size, weight, material, and pressure resistance.


# Meeting 1:

Date: 03/12/23
Time: 9:15 - 12 PM

Reference Material: https://ecetechprojects.wordpress.com/2011/07/08/arduino-h-bridge-motor-control/

Finalized Proposal: https://1drv.ms/w/s!At5nmv7gLyVwkvE4l1jkQC4PCUBfSg?e=4K8k71

Discussed the H-Bridge Design and decided which parts would be used
  - Decided on using PNP transistors
  - 9V battery
  - DC motors
  
Went through the schematic and calculated how much current it could handle

Defined and divided up the tasks

<img src="https://user-images.githubusercontent.com/69320369/224601874-c5b4059b-2ab1-4c97-a3c2-f3a50a5f6dbe.png" height="300" />

# Meeting 2:

Date: 03/18/23
Time: 2 - 8 PM

Sam provided a simple schematic with transistors. We then decided to change the circuit to mosfets because VCC is higher than the gate voltages and because the mosfets have built-in reverse-bias diodes to help with overvoltage spikes when the car is braking. After we did that, we realized we still needed an NPN transistor to control the mosfets. The new circuit has 4 mosfets and 2 transistors. We used 10kohm pull-up resistors on the P-channel gates to latch them shut. According to our math this means we'll have ~0.1mA through the transistors. This will affect which resistor we put on the transistors bases. For now it's 2.2k but we might need to increase that a bit to 10k as well for less current on the base.

Using a 10k resistor  in series with the 2N2222 Collector, we will see around 1mA, assuming 10V from the battery. Using a 2.2k resistor in series with the 2N2222 Base, we see 1.4mA, assuming 3.0v from the Pi. Given these parameters, we will expect <0.1V from the collector to emitter, so the MOSFET Gates will be basically grounded when the respective PI pin is HIGH. Conversely, in order flip the MOSFET gates HIGH, current into the base will need to be <7nA. Assuming we're using the 2.2k resistor, the PI output pin must be at <0.0154V relative to ground. In the real world, this might prove difficult, and testing will be required.

<img src="https://user-images.githubusercontent.com/69320369/226380973-0f21aae3-170d-4731-864c-b7e31b808524.png" width="400" />

Updated TinkerCad:

<img src="https://user-images.githubusercontent.com/69320369/226380291-c77ee0eb-ffea-4c81-8b9d-a37d5abbd992.png" width="400" />

Parts List:
VBatt = 5v ~ 12v
RPullup = 10k
I_Collector = .5mA ~ 1.2mA
beta(max hFE) = 50
I_base = 10nA ~ 24nA
I_max = 16mA (Max PI Output)
V_Output = 3.0V ~ 3.3V 
R_BaseNPN = 2.2k
I_Output = 1.4mA ~ 1.5mA

# Meeting 3:

Date: 03/19/23
Time: 5 - 9 PM

Sam designed a chassis and printed it. The code is practically done we just need to do the GPIO assignments once we build the circuit. As for the power system we are using a 9.6V 2000 mAh battery with a voltage regulator for the H bridge circuit and a voltage regulator to power the pi with 5V. The remaining parts were also bought. 

<img src="https://user-images.githubusercontent.com/69320369/226381850-392b5e93-d138-4c30-b5b8-187398b2b5b0.png" height="300" />

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

<img src="https://media.discordapp.net/attachments/1070823721411018833/1089547193486155896/20230326_084949.jpg?width=312&height=553" height="300" /> <img src="https://media.discordapp.net/attachments/1070823721411018833/1089547193167380491/20230326_084758.jpg?width=312&height=553" height="300" /> 

 We discussed which controller we would use to control the robot. We could connect an Xbox controller with analog thumb sticks using bluetooth or use a numpad with different numbers signalling different speeds. We need to work on the code so we can program the directions using the following table:
 
<img src="https://media.discordapp.net/attachments/1070823721411018833/1089817415908610108/image.png?width=535&height=555" height="300" /> <img src="https://media.discordapp.net/attachments/1070823721411018833/1089819112106115112/rn_image_picker_lib_temp_2e97c4f8-33c7-49ef-ae3b-879236283686.jpg?width=312&height=553" height="300" />

Current version of the schematic:

<img src="https://user-images.githubusercontent.com/69320369/229191431-44b014b4-56c6-40b3-8c9d-de0a184eca29.png" height="300" /> <img src="https://user-images.githubusercontent.com/69320369/229191877-9a6d93dd-2410-4f10-ad3c-a063bb9ff0b6.png" height="300" />


# Meeting 6:

Date: 03/30/23
Time: 2:30 - 5 PM

Reference Material: https://learn.adafruit.com/improve-brushed-dc-motor-performance/pwm-and-brushed-dc-motors

Finalized Working TinkedCad Circuit: https://www.tinkercad.com/things/bnNonHPksck-fantastic-hillar/editel?sharecode=lQiAWzKQ8pHRZROjkhvst0w-F3ZCxrJRO_LkxZTcMJo

The rover circuit was built on a separate breadboard for testing and we got 1 wheel working. We will eventually build the circuit on the breadboard that is already attached to the rover. The flyback diode in the circuit and the mosfets fixed the spikes that appeared when using PWM. Most of the code was written and added to the github repository. 

<img src="https://user-images.githubusercontent.com/69320369/229192614-bd41dcf6-abbb-4d40-9a7c-6549bf6996ab.png" height="300" /> <img src="https://user-images.githubusercontent.com/69320369/230246072-87da07ba-cce4-4893-94e3-b1aad60b3247.png" height="300" />




