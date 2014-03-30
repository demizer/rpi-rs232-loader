============
RS232 Loader
============

This is a small python script used to send programs Gcode programs to a CNC
over RS232 using a Raspberry Pi.

Requirements
============

* `Arch Linux Arm`_
* Python 3.2+
* rpio_
* pyserial_

How to use it
=============

See http://demizerone.com/articles/rpi-rs232-loader for a complete build guide.

The script must be run as root. Copy the project to the /root directory and
work from there.

.. code:: sh

    # python loader.py

To run the script on startup, enable the systemd module:

.. code:: sh

    # cp rs232-loader.service /etc/systemd/system
    # systemctl start rs232-loader.service

Authors
=======

Jesus Alvarez (jeezusjr@gmail.com)

.. _Arch Linux Arm: http://archlinuxarm.org/
.. _rpio: https://aur.archlinux.org/packages/rpio/
.. _pyserial: https://www.archlinux.org/packages/community/any/python-pyserial/

