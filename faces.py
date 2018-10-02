from flask import Flask, jsonify, make_response, request, abort, redirect, send_file
import logging

import emotion_gender_processor as eg_processor
import base64
import json
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://ekholabs.ai", code=302)

@app.route('/classifyImage', methods=['POST'])
def upload():
    try:
        image = ''
        if 'application/json' in request.content_type:
            image = base64.b64decode(request.get_json()['image'])
        elif 'multipart/form-data' in request.content_type:
            image = request.files['image'].read()
        else:
            image = base64.b64decode(request.get_data())
        faces = eg_processor.process_image(image)

        response = make_response(jsonify(faces), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as err:
        logging.error('An error has occurred whilst processing the file: "{0}"'.format(err))
        abort(400)

@app.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)