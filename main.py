from flask import Flask, render_template, request
import requests

URL = 'https://api.github.com/users/cparragatorres'

app = Flask(__name__)

@app.route('/')
def index():
    data = requests.get(URL)
    context = data.json()
    print(context)
    
    return render_template('index.html', **context)

################### RUTAS DE MIS PAGINAS #####
@app.route('/acercade')
def about():
    return render_template('acercade.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug = True) #RunApplication