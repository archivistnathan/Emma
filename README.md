# Environmental Monitoring and Management for Archives

> [!NOTE]
> The proliferation of low cost all-in-one solutions has rendered this project obsolete. Please refer to the list of alternative devices instead.

## Alternative Devices
+ [Enviro Indoor](https://shop.pimoroni.com/products/enviro-indoor?variant=40055644717139) - this is a stand-alone solution that monitors temperature, humidity, pressure, VOCs, VSCs, light intensity, and CO2 via a optional sensor. The use of the lower powered Pico W solves the power and heat issues of the original project.
+ [Enviro Urban](https://shop.pimoroni.com/products/enviro-urban?variant=40056508252243) - another Enviro variant which monitors temperature, humidity, pressure, and particulate matter concentration.
+ [Pico Enviro+](https://shop.pimoroni.com/products/pico-enviro-pack?variant=40045073662035) - this requires a separate Pico or Pico W but offers an on-board screen for reading values
+ Elitech USB Data Loggers (https://www.amazon.co.uk/s?srs=94209968031) - I am still experimenting with these so I do not formally endorse them. However, they are cheap options if you only need to log the temperature and humidity and don't want to mess around with Python.

## Introduction

The Environmental Monitoring and Management for Archives (EMMA) project aims to develop an open source, low-cost, low maintenance system to monitor vital environmental statistics to aid in the preservation of archives. With a target cost of around £100, EMMA is not intended to have the same feature set as currently available data loggers but is instead aimed at small cultural heritage centres and institutions will archival stores that do not have ready access to calibration equipment or expensive environmental monitors. EMMA is intended to serve as an early warning device to inform conservation decisions and to potentially initiate necessary remedial action earlier that would otherwise be the case once an issue has been identified.

EMMA is based on the Raspberry Pi, chosen for its widespread availability, ease of use, and the proliferation of pre-existing Python code to interface with the chosen sensor modules. As mentioned, the RPi runs Python code to gather measurements then transmits them to a database server. There is fundamentally no new code in this project, just reappropriation of existing code for a specific archives use case.

The sensors are chosen given a desired set of environmental conditions to be monitored, namely:
- temperature (degrees Celsius)
- relative humidity (%RH)
- visible light level (lux)
- UV light level (WHO UV Index)
- shock / vibration (g)
- ambient noise level (relative scale)
- air quality / smoke / combustible gas (relative scale converted to ppm)
- user / visitor count (integer)

The main considerations for sensor selection is cost and the ready availability of integrated modules. EMMA is designed as a DIY project that any archive can build. Thus while the use of discrete components on a custom designed PCB hat to connect directly to the RPi would have resulted in a much more compact form factor, the decision was made in favour of pre-built modules to minimise fabrication requirements and reduce the necessary know-how as some institutions that would benefit from the project may not necessarily know how to design and fabricate a PCB. Unfortunately because of the way some modules are packaged a little soldering is still required to attach connector pins. The ability to read circuit diagrams, or at least the ability to identify and connect module pins to RPi pins is of course required.

EMMA has two main outputs: a buzzer and a tri-colour led. There is also a relay output (expandable) to trigger external devices or actions. The program mas also be customised to use IFTTT and interface with IoT devices.

EMMA is a project of Prof. Jonathan Isip at the University of the Philippines School of Library and Information Studies (UP SLIS).

## System Requirements
- Raspberry Pi 3 B+ or later
- 3A power supply or higher
- Sensor modules

## Known Limitations
Power - the system is limited by a wired power connection to the RPi. This makes it susceptible to power outages and limits placement options. A PiJuice HAT or similar device can conceivably be attached to provide battery power but this would not last more than a day before needing recharging.

Thermals - The RPi is a computer which emits heat. The temperature sensors should not be placed in closed proximity to the board. Use a fan to dissipate heat to the room at large. If monitoring an enclosed space such as a display case use cable connectors to keep sensors inside the case and the RPi outside.

Sensor calibration - The system readings are limited by the accuracy of the sensor modules. These sensors drift over time due to their physical and chemical characteristics. The chosen low-cost sensor modules cannot be easily recalibrated. Set up the build such that these modules can easily be swapped with new ones. Regularly compare readings with professional meters to 
check if still acceptable. If professional meters are not available sanity check the readings and remember that for most physical media temperature and humidity fluctuation causes more damage than sustained high or low temperatures. The code also relies on redundancy and sensor diversity to validate the accuracy of readings. E.g. Temperature is read from DS18B20+, DHT11, and DHT22 sensors. At least two of the readings should be within 0.5 degrees Celsius of each other for the measurement to be considered valid and logged to the database.
