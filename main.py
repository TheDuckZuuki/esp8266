from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from time import sleep


def connectLcd():
  i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
  devices = i2c.scan()
  if len(devices) == 0:
    raise NameError("No i2c device !")
  return I2cLcd(i2c, devices[0], 4, 20)


lcd = connectLcd()

while True:
  lcd.move_to(0, 0)
  lcd.putstr("Line 1")
  lcd.move_to(0, 1)
  lcd.putstr("Line 2")
  lcd.move_to(0, 2)
  lcd.putstr("Line 3")
  lcd.move_to(0, 3)
  lcd.putstr("Line 4")


"""
lcd.clear()
lcd.write("Line 1")
lcd.move_to(0, 0)

sleep(2)
"""
