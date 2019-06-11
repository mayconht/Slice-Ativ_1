from flask import Flask, request
import json
import os

app = Flask(__name__)
time = []

def dockerstats():
    return os.system("docker stats --no-stream")
    


@app.route('/GET_INFO', methods=['GET'])
def home():
    dockerstats();
    return json.dumps(time, indent=4), 200


@app.route('/POST_INFO', methods=['POST'])
def time_per_lang():
    if not request.json:
        return json.dumps("ERRO: Verifique se o post feito esta no formato Json"), 400
    time.append(request.json)
    return json.dumps("Sucesso: execute o metodo Get para ver os dados"), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')