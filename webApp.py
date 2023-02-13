from flask import Flask, url_for, request, render_template, jsonify
import requests
import json

app = Flask(__name__)
 
@app.route('/')
def index():
   return render_template ('index.html')


@app.route("/wetter", methods = ['POST', 'GET'])
def wetter():
   global stadt
   temperature = ''
   if request.method == "POST":
      stadt = request.form['stadt']

      api_key = "f37908b35efdf1d8201b485bd80510ab"
      url = f"http://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={api_key}"


      response = requests.get(url).json()
      # get current temperature and convert it into Celsius
      current_temperature = response.get('main', {}).get('temp')
      if current_temperature:
         current_temperature_celsius = round(current_temperature - 273.15, 2)
         return render_template('temperature.html', stadt = stadt.title(), temperature = current_temperature_celsius)

      else:
         return f'Error getting temperature for {stadt.title()}'

   else:
      return 'Fehler'

@app.route('/uhrzeit')
def uhrzeit():
   response = requests.get(
      f"https://timezone.abstractapi.com/v1/current_time/?api_key=fbdee759315c4fffa16bfd803165e9fd&location={stadt}, Germany")

   return render_template('uhrzeit.html', stadt = stadt, data = response.content)

@app.route('/telefon', methods = ['POST', 'GET'])
def telefon():
   if request.method == "POST":
      phonenumber = request.form['phone']
      response = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=0101f196083747b1a874bf6734f99a37&phone={phonenumber}")
      return response.content

   else:
      return 'Fehler'


if __name__ == '__main__':
   app.run(port = 1337, debug= True)