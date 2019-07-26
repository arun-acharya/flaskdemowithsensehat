import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from sense_hat import SenseHat


app = Flask(__name__) #starting flask
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sense = SenseHat()
#define actuators GPIOs
fan = 21
led = 26



# Define pins as output
GPIO.setup(fan, GPIO.OUT)    
GPIO.setup(led, GPIO.OUT) 

# turns OFF at startup 
GPIO.output(fan, GPIO.LOW)
GPIO.output(led, GPIO.LOW)
	
@app.route("/")#creation of landing page
def index():
	# Read Sensors Status
	humidity =  round (sense.get_humidity(), 2)
	temperature = round (sense.get_temperature(), 2)
	pressure = round (sense.get_pressure(), 2)
        #storing into variables to pass to html file
	templateData = {
              'temp'  : temperature,
              'humi'  : humidity,
              'pres' : pressure,
              
       }
	return render_template('index.html', **templateData)   #redirecting landing page to use external file and passing data to itled'  : ledSts,
              
if __name__ == "__main__": #starts flask server on specified IP address
   app.run(host="0.0.0.0", port=80, debug=True)

        


