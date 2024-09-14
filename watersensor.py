from Machine import Pin, ADC
sensor = ADC(Pin(26))
led = Pin(28, Pin.OUT)
timer = Timer()

def toggle_water_drip(condition):
    if condition == 1:
        turn_on_water()
    elif condition == 0:
        turn_on_water()
        
def turn_on_water():
    pass

def turn_off_water():
    pass

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

reading = sensor.read_u16()
if reading < 400:
   condition = 1
else:
    condition = 0
