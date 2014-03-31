#!/usr/bin/env python3

import sys
import time
import datetime

import RPIO

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject

print("loader.py started")

# A list containing Drive objects that are found on the system.
DRIVES = []


class Drive:
    """Object contaning a usb removable flash drive."""

    def __init__(self, drive_object_path, drive_properties, block_path,
                 block_properties ):
        self.object_path = drive_object_path
        self.properties = drive_properties
        self.block_path = block_path
        self.block_properties = block_properties
        self.mount_location = ""


    def path(self):
        """Return the dbus object path for the drive."""
        return self.object_path


    def mount_point(self):
        """Returns the mount point of the drive."""
        if self.mount_location:
            return self.mount_location
        fs = self.block_properties.get('org.freedesktop.UDisks2.Filesystem')
        mp = fs.get('MountPoints')
        self.mount_location = bytearray(mp[0]).decode('latin-1')
        return self.mount_location


    def files(self):
        """Returns a list of files on the drive."""
        pass


    def has_file(self, filename):
        """Returns absolute file path if filename exists on the drive."""
        pass


    def has_file_ignore_extension(self, filename):
        """Returns absolute file path if filename exists on the drive.

           File extensions are ignored.

        """
        pass


class DBusManager:
    """A manager of DBus objects."""

    def __init__(self):
        self.bus = dbus.SystemBus(mainloop=DBusGMainLoop())
        self.dbus_obj = self.bus.get_object("org.freedesktop.UDisks2", "/org/freedesktop/UDisks2")
        self.dbus_manager = dbus.Interface(self.dbus_obj, "org.freedesktop.DBus.ObjectManager")

        # Set callbacks for signals when new drives are mounted
        self.dbus_manager.connect_to_signal("InterfacesAdded", self._on_interfaces_added)
        self.dbus_manager.connect_to_signal("InterfacesRemoved", self._on_interfaces_removed)


    def _on_interfaces_added(self, object_path, interfaces_and_properties):
        """TODO"""
        print("Interface added!", object_path)


    def _on_interfaces_removed(self, object_path, interfaces):
        """TODO"""
        print("Interface removed!", object_path)


    def get_drives(self):
        """Uses dbus to get available drives."""
        drives = []
        # Check for usb drives that are already mounted
        managed_drives = self.dbus_manager.GetManagedObjects().items()
        for obj, val in managed_drives:
            drive_info = val.get('org.freedesktop.UDisks2.Drive', {})
            if drive_info.get('ConnectionBus') == 'usb' and drive_info.get('Removable'):
                # We have the drive, now we need the block device...
                for bdev, val2 in managed_drives:
                    block_dev = val2.get('org.freedesktop.UDisks2.Block', {})
                    if block_dev.get('Drive') == obj and block_dev.get('IdUUID'):
                        drives.append(Drive(obj, val, bdev, val2))
        return drives


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
    for drive in manager.get_drives():
        print("Mount point for", drive.path(), drive.mount_point())

    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()


if __name__ == "__main__":
    main()
