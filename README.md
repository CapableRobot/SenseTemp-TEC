# SenseTemp TEC

Designed by [Capable Robot Components](http://capablerobot.com).  
Follow us on [Twitter](http://twitter.com/capablerobot) for product announcements and updates.

---

**SenseTemp TEC is available for purchase at [CrowdSupply](https://www.crowdsupply.com/capable-robot-components/sensetemp) & [Mouser](https://www.mouser.com/ProductDetail/Crowd-Supply/cs-sensetemp-03?qs=sGAEpiMZZMsSgQ5oX0A7uhzs7btMGoRQYlEWJtksaKTgK6BSOcNH6Q%3D%3D).**  

## SenseTemp TEC Features 

## Specifications

## Feather Hosts

SenseTemp TEC is designed to mate with Adafruit Feather-compatible host modules, like:

* [Adafruit Feather M4 Express](https://www.adafruit.com/product/3857)
* [Adafruit Feather M0 Express](https://www.adafruit.com/product/3403)
* [Adafruit ESP32 Feather Host](https://www.adafruit.com/product/3405)

Note that the ES8266 Feather is **NOT** supported due to the limited IO on the ESP8266.  It does not have enough pins to support the four SPI devices of the SenseTemp.

## Software

## Hardware Revisions

* [CR2ERP](revisions/CR2ERP) : Released 2018-12-18.
	* Added high-side switch for fan control
	* Removed `!EN` pin as this product will not run off of battery power and there is no need to disable RTD converter chips.
	* Added 12v to 3v regulator (and disabled 5v to 3v regulator on host board).
	* Minor footprint changes.
	* Changed `PWM` pin for TEC control.
* [CRHVEF](revisions/CRHVEF) : Initial version released 2018-12-04.

## License Information

| **Type** | **License** |
| --- | --- |
| Hardware | Copyright Capable Robot Components 2018 <br><br>This documentation describes Open Hardware and is licensed under the [CERN OHL v1.2 or later](https://www.ohwr.org/licenses/cern-ohl/license_versions/v1.2). <br/><br/> You may redistribute and modify this documentation under the terms of the CERN OHL v.1.2.  This documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN OHL v.1.2 for applicable conditions |
| Software | [MIT License](tree/master/LICENSE.txt) |
| Documentation | [Creative Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-sa/4.0/) License |

More detailed information about the CERN License is available in the [license](license) folder and on the [CERN website](https://www.ohwr.org/projects/cernohl/wiki).


| **OSHW Certification** |

Coming Soon