#!/usr/bin/env python3

import sys
import time
import datetime

import RPIO

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject


print("loader.py started")


class Drives:
    def __init__(self):
        pass

class DBusManager:
    """A manager of DBus objects."""

        self.dbus_obj = bus.get_object("org.freedesktop.UDisks2", "/org/freedesktop/UDisks2")
        self.dbus_manager = dbus.Interface(obj, "org.freedesktop.DBus.ObjectManager")
    def __init__(self):
        self.bus = dbus.SystemBus(mainloop=DBusGMainLoop())
        # managed_objects = manager.GetManagedObjects()
        self.dbus_manager.connect_to_signal("InterfacesAdded", self._on_interfaces_added)
        self.dbus_manager.connect_to_signal("InterfacesRemoved", self._on_interfaces_removed)
        self.drives = Drives()

    def _on_interfaces_added(self, object_path, interfaces_and_properties):
        """TODO"""
        print("Interface added!", object_path)


    def _on_interfaces_removed(self, object_path, interfaces):
        """TODO"""
        print("Interface removed!", object_path)


class RpiIO:
    """An object to manage input/output from the Raspberry Pi."""

    def __init__(self):
        pass
        # RPIO.setmode(RPIO.BOARD)

        # RPIO.setup(11, RPIO.IN) # Pull down resistor connected to ground
        # RPIO.setup(16, RPIO.OUT)

        # # blinking function
        # def blink(pin):
                    # RPIO.output(pin, RPIO.HIGH)
                    # time.sleep(0.1)
                    # RPIO.output(pin, RPIO.LOW)
                    # time.sleep(0.1)
                    # return

        # pushCounter = 0
        # lastState = False
        # buttonState = False
        # lastEvent = datetime.datetime.now()

        # try:
                # while True:
                    # buttonState = RPIO.input(11)
                    # if buttonState != lastState:
                        # if buttonState:
                            # pushCounter += 1
                            # time.sleep(0.17)
                            # lastEvent = datetime.datetime.now()
                    # lastState = buttonState
                    # if pushCounter > 0 and (datetime.datetime.now() - lastEvent).seconds > 1:
                        # print("Button pressed", pushCounter, "times.")
                        # pushCounter = 0
        # except (KeyboardInterrupt, SystemExit):
                # print("Goodbye!")
        # finally:
                # RPIO.cleanup()


def main():
    loop = GObject.MainLoop()
    manager = DBusManager()
    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()


if __name__ == "__main__":
    main()
