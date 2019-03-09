import requests
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():

        if request.method == 'GET':
         city = request.args.get('city')

        city = 'mumbai'
        #print(city)
        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1').json()
   


        data={
         'city':city,
         'temperature': req['main']['temp'],
         'desc': req['weather'][0]['description'],
         'icon': req['weather'][0]['icon'],
        }

        print(data)

        return render_template('index.html', data=data)
if __name__ == '__main__':
   app.run()
