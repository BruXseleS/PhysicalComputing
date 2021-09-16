import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) 
class LED:
    def __init__(self, pin):
        self.pin = pin
        self.leuchtet = False
        GPIO.setup(pin, GPIO.OUT)
        self.auschalten()
    
    def anschalten(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.leuchtet = True
    
    def auschalten(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.leuchtet = False
   
    def ist_an(self):
        return self.leuchtet 
    
    def toggle(self): 
       while True:
        if Taster.ist_gedruckt == True:
            self.anschalten()
            print("led ist an")
class Taster:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)
    def ist_gedruckt(self):
        'Prüft, ob der Taster gedrückt ist (True) oder nicht (False).'
        if GPIO.input(self.pin, IN) == True:
          print("Taster gedruckt")
        return GPIO.input(self.pin, GPIO.IN)  



           


grun = LED(13)
taster1 = Taster(12)
grun.toggle()
GPIO.cleanup()
taster1.ist_gedruckt()
