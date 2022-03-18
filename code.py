## you data need to be a list with decimal values (bytes converted in decimal)

## EX:   data = [0xFA, 0x6D, 0xB6] you data need is -> data = [250, 109, 182]

## this code use a poly = 0x1021, you can change for you poly

def crc16(data):
    crc = 0xFFFF
    for i in data:
        crc ^= i << 8
        for j in range(0,8):
            if (crc & 0x8000) > 0:
                crc =(crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return crc & 0xFFFF
