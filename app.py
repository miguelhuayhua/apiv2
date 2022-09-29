import json
from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def hello():
    return "Hello world"



@app.route('/data')
def getData():
    return jsonify([
        {'nombre':'Salchipapa',
        'img':'https://decomidaperuana.com/wp-content/uploads/2020/04/salchipapa.jpg',
        'descripcion':'La salchipapa es una comida rápida que consiste en rodajas fritas de salchicha y papas fritas, consumida como comida rápida en Hispanoamérica.'
        },
        {'nombre':'plato paceño',
        'img':'https://placeresbolivia.com/wp-content/uploads/2021/09/PLATO-PACENO.jpg',
        'descripcion':'El plato paceño es un plato tradicional del departamento de La Paz, Bolivia.'},
        {'nombre':'mondongo',
        'img':'https://www.cocina-boliviana.com/base/stock/Recipe/445-image/445-image_web.jpg',
        'descripcion':'El mondongo es un platillo boliviano que conocemos por ser típico de la región chuquisaqueña. Con un sabor delicioso, consta de un tipo de caldo con mote de maíz cocido, piel de chancho y ahogado que acompañan a la carne de chancho.'},
        {'nombre':'pique macho',
        'img':'https://chipabythedozen.com/wp-content/uploads/2020/07/Pique-Macho-Bolivia.jpg',
        'descripcion':'El pique macho o pique a lo macho es un plato típico de Bolivia. Consiste en trozos de carne de vaca y patatas fritas. También se le añade cebolla, locoto, huevos duros, queso cortado, mostaza, mayonesa y kétchup.'}
    ])