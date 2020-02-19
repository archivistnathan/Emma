# htu21d
**Python 2.7** library for the Adafruit HTU21D-F Humidity and Temperature sensor breakout board. https://www.adafruit.com/product/1899

Based on the code of the Adafruit_Python_HTU21D library written by Massimo Gaggero for Adafruit Industries.

The original Adafruit library only partially supports **Python 2.7**, which I am using for my Raspberry Pi-Weatherstation-Project.Therefore, I had to modify the library for full support of **Python 2.7**. 

Additionally, I replaced the original function 'read_dewpoint()' by the function 'dewpoint()', which now can be called with temperature and humidity as parameters. If the function is called without passing the temperature and/or the relative humidity, the function reads the sensors current value(s).

For higher accuracy, the dew point is now calculated based on an algorithm published by *Stefan Ochs*. This algorithm distinguishes temperatures above or equal to 0 deg. Celsius from temperatures below 0 deg. Celsius. For further information see: https://www.wetterochs.de/wetter/feuchte.html
 
**Warning**:

 * tested only on ***RPi-3*** running ***Raspbian Stretch*** and ***Python 2.7***.
 * for additional warnings, see https://github.com/mgaggero/Adafruit_Python_HTU21D

## Installation
### Setuptools
The following commands install the library system wide:
```console
git clone https://github.com/HoK-matic/htu21d.git
cd htu21d
sudo python setup.py install
```

## Permissions and privilieges
Accessing **I2C** devices usually requires root privileges or privileged group membership. These can be obtained with:

* the use of `sudo` to run the program;
* adding the user that runs the program to the I2C's device owning group, if exists.

## Usage
```python
>>> import htu21d.htu21d as htu

>>> sensor = htu.HTU21D()

>>> sensor.read_temperature()
22.2919711914062

>>> sensor.read_humidity()
53.1524365234375

>>> sensor.dewpoint()
12.3014062484367

>>> sensor.reset()

```
