import logging
from flask import Flask, request, jsonify

# Configuration du logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')

def home():
    logging.info("Accueil accédé")
    return jsonify({'message': 'Ici Mon API'})


@app.route('/error')
def error():
    try:
        raise ValueError("Une erreur simulée")
    except ValueError as e:
        logging.error(f"Erreur capturée: {e}")
        return "Une erreur est survenue", 500



@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    logging.debug(f"Adding: {data['a']} + {data['b']} = {result}")
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    logging.debug(f"Subtracting: {data['a']} - {data['b']} = {result}")
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

    
