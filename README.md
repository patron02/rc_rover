# rc rover

The goal of this project is to design and prototype an RC rover that can move in all directions to explore terrain. A rover is used to collect information and samples from a specific terrain. They are used by lots of companies, especially those focused on space or deep-sea exploration. Some specifications that we might need to consider are: size, weight, material, and pressure resistance.


**Meeting 1:
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

<img src="https://user-images.githubusercontent.com/69320369/224601874-c5b4059b-2ab1-4c97-a3c2-f3a50a5f6dbe.png" width="400" />

**Meeting 2:
Date: 03/18/23
Time: 2 - 8 PM

Sam provided a simple schematic with transistors. We then decided to change the circuit to mosfets because VCC is higher than the gate voltages and because the mosfets have built-in reverse-bias diodes to help with overvoltage spikes when the car is braking. After we did that, we realized we still needed an NPN transistor to control the mosfets. The new circuit (pinned on Discord) has 4 mosfets and 2 transistors. We used 10kohm pull-up resistors on the P-channel gates to latch them shut. According to my math (also pinned) this means we'll have ~0.1mA through the transistors. This will affect which resistor we put on the transistors bases. For now it's 2.2k but we might need to increase that a bit to 10k as well for less current on the base.

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

**Meeting 3:
Date: 03/19/23
Time: 5 - 9 PM

Sam designed a chassis and printed it. The code is practically done we just need to do the GPIO assignments once we build the circuit. As for the power system we are using a 9.6V 2000 mAh battery with a voltage regulator for the H bridge circuit and a voltage regulator to power the pi with 5V. The remaining parts were also bought. 

<img src="https://user-images.githubusercontent.com/69320369/226381850-392b5e93-d138-4c30-b5b8-187398b2b5b0.png" width="400" />




