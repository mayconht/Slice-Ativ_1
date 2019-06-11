from flask import Flask, request
import json
import os
import requests

app = Flask(__name__)
time = []

def dockerstats():
    r = requests.post('http://192.168.2.100:5000/POST_INFO', json=os.system("docker stats --no-stream"))
    time.append(r.json)
    return ("data posted to server", time)
    


@app.route('/GET_INFO', methods=['GET'])
def home():
    dockerstats()
    return dockerstats(), 200


@app.route('/POST_INFO', methods=['POST'])
def time_per_lang():
    if not request.json:
        return json.dumps("ERRO: Verifique se o post feito esta no formato Json"), 400
    time.append(request.json)
    print(request.json)
    return json.dumps("Sucesso: execute o metodo Get para ver os dados"), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')