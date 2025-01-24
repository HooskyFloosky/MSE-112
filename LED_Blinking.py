import pigpio
import time 

pi = pigpio.pi()

if not pi.connected:
    print("Failed to Connect")
    exit()

LED_PIN = 17

pi.set_mode(LED_PIN, pigpio.OUTPUT)

try:
    while True:
        pi.Write(LED_PIN,1)
        time.sleep(1)
        pi.Write(LED_PIN,0)
        time.sleep(0)
except KeyboardInterrupt:
    pi.write(LED_PIN,0)
    pi.stop
    print("Program Terminated")
    print("Have fun!")