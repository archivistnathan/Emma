# Environmental Monitoring and Management for Archives

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

## System Requirements
- Raspberry Pi model 3 B+ or later
- 3A power supply or higher
- Sensor modules

EMMA is a project of Prof. Jonathan Isip at the University of the Philippines School of Library and Information Studies (UP SLIS).
