from machine import UART, Pin, I2C
from time import sleep
import oledlib

# ====== GPS UART ======
gps = UART(2, baudrate=9600, tx=17, rx=16, timeout=1000)

# ====== OLED ======
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = oledlib.SSD1306_I2C(128, 64, i2c)

# ====== UBX Commands to enable NMEA ======
enable_gga = b'\xB5\x62\x06\x01\x08\x00\xF0\x00\x01\x01\x00\x00\x00\x00\xFA\x0F'
enable_rmc = b'\xB5\x62\x06\x01\x08\x00\xF0\x04\x01\x01\x00\x00\x00\x00\xFE\x17'

gps.write(enable_gga)
sleep(0.1)
gps.write(enable_rmc)
sleep(0.1)

oled.fill(0)
oled.text("GPS Init...", 5, 10)
oled.show()

print("NMEA enabled, starting read loop...")


# ====== Function: Convert NMEA → Decimal Degrees ======
def convert_to_decimal(raw, direction):
    try:
        deg = float(raw[:2])
        minutes = float(raw[2:])
        decimal = deg + (minutes / 60)
        if direction in ['S', 'W']:
            decimal *= -1
        return round(decimal, 6)
    except:
        return None


# ====== MAIN LOOP ======
lat = None
lon = None

while True:
    if gps.any():
        line = gps.readline()

        if not line:
            continue

        try:
            text = line.decode('utf-8', errors='ignore').strip()
        except:
            text = ""

        print("RAW:", line)
        print("TXT:", text)

        # ====== Parse GGA ======
        if text.startswith("$GPGGA"):
            parts = text.split(',')
            if len(parts) > 5 and parts[2] and parts[4]:
                lat = convert_to_decimal(parts[2], parts[3])
                lon = convert_to_decimal(parts[4], parts[5])

        # ====== Parse RMC ======
        if text.startswith("$GPRMC"):
            parts = text.split(',')
            if len(parts) > 5 and parts[3] and parts[5]:
                lat = convert_to_decimal(parts[3], parts[4])
                lon = convert_to_decimal(parts[5], parts[6])

    #
