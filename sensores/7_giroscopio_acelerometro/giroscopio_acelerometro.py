# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    ax, ay, az = mpu.acceleration
    gx, gy, gz = mpu.gyro

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    #print((ax, ay, az, )) #Plotter acceleration

    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print((gx, gy, gz, )) #Plotter gyroscope

    print("Temperature: %.2f C" % mpu.temperature) #Temperature

    time.sleep(0.05)