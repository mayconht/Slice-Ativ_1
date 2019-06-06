from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Maycon',
        'lang': 'python'
    },
    {
        'id': 2,
        'name': 'Willian',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'Jaime',
        'lang': 'python'
    }
]

@app.route('/group', methods=['GET'])
def home():
    return jsonify(devs), 200


@app.route('/group/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200


@app.route('/group/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200

    return jsonify({'error': 'not found'}), 404


@app.route('/group', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)

    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)
