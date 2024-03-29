from flask import Flask, request, jsonify, Response
import json
from Jugador import Jugador

app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
	status = {"status": "OK"}
	return json.dumps(status)

@app.route('/status', methods=['GET'])
def estado():
	status = {"status": "OK"}
	return json.dumps(status)

@app.errorhandler(404)
def page_not_found(e):
	return jsonify(error=str(e)), 404

#http://0.0.0.0:5000/Expectancia?elojug1=1500&elojug2=1800
@app.route('/Expectancia', methods=['GET'])
def func1():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')

	Jugador1 = Jugador(int(parametro1))
	Jugador2 = Jugador(int(parametro2))
	
	valor = str(Jugador1.getExpectancia(Jugador2.elo))
	data = {}
	data['expectancia'] = valor

	return Response(json.dumps(data), mimetype='application/json')

#http://0.0.0.0:5000/NuevoElo?elojug1=1500&elojug2=1800&k=40&resultado=1
@app.route('/NuevoElo')
def nuevo_elo():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')
	parametro3 = request.args.get('k')
	parametro4 = request.args.get('resultado')

	Jugador1 = Jugador(int(parametro1))
	Jugador1.k = int(parametro3)
	Jugador2 = Jugador(int(parametro2))
	
	valor = str(Jugador1.getNuevoElo(int(parametro2), int(parametro4) ))
	data = {}
	
	data['nuevoElo'] = valor

	return Response(json.dumps(data), mimetype='application/json')

