# Milus
Miniluftschiff

Steps to install on esp32
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --chip esp32 write_flash -z 0x1000 esp32-ppp-fix.bin

ampy -p /dev/ttyUSB0 put Milus/ /
