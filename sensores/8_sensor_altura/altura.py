import time
import board
# import digitalio # For use with SPI
import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# OR Create sensor object, communicating over the board's default SPI bus
# spi = board.SPI()
# bmp_cs = digitalio.DigitalInOut(board.D10)
# bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi, bmp_cs)

# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25
while True:
    print("\nTemperature: ", bmp280.temperature, "C")
    print("\nPressure: ", bmp280.pressure, "\nhPa")
    print("Altitude: ", bmp280.altitude, "meters")
    print((bmp280.temperature, bmp280.pressure, bmp280.altitude, )) #Plotter variables
    time.sleep(0.05)