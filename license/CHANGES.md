Here we are compiling a community changelog.

If you come up with a modification of our designs, please share it
with the community, log your changes below, and upload the files to
our GitHub repository.

# Change Format

**NAME** on DATE by *Your name*.
Description of modification

# Change Log

* **[CR2ERP](https://github.com/CapableRobot/SenseTemp/tree/master/revisions/CR2ERP)** on 2018-12-18 by *Chris Osterwood*
	* Added high-side switch for fan control
	* Removed `!EN` pin as this product will not run off of battery power and there is no need to disable RTD converter chips.
	* Added 12v to 3v regulator (and disable 5v to 3v regulator on host board).
	* Minor footprint changes.
	* Changed `PWM` pin for TEC control.
	* Add user LED near RTD connector.
* **[CRHVEF](https://github.com/CapableRobot/SenseTemp/tree/master/revisions/CRHVEF)** 2018-12-04 by *Chris Osterwood*