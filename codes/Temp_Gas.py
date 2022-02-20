import bluetooth
import os

print(os.uname())
devices = bluetooth.discover_devices(lookup_names=True)

print(devices)
