import requests
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
   city = 'Mumbai'
   if request.method == 'GET':
      city = request.args.get('city')
   #print(city)
   req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1').json()
   
   print(req)
   return render_template('index.html')

if __name__ == '__main__':
   app.run()