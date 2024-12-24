# f = open('Firmware/Firmware1/OTA.bin', 'rb')
with open('Firmware/Firmware1/OTA.hex', 'rb') as f:
    lines = f.readlines()
    for i in lines:
        print(i)