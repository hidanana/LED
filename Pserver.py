import socket               
import RPi.GPIO as GPIO
import time


s = socket.socket()         
host = socket.gethostname()       
port = 12345                
s.bind((host, port))        

print"Waiting for connections. . ."

s.listen(5)                 
while True:
   c, addr = s.accept()     
   print 'Got connection from', addr
   c.send('ThankS for connecting')
   print"LED IS ON"
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(27,GPIO.OUT)
  
   GPIO.output(27,GPIO.HIGH)
   time.sleep(4)
   print"\n LED IS OFF"
   GPIO.output(27,GPIO.LOW)
   
   c.shutdown(1)
   c.close()            

