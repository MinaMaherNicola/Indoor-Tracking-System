import joblib
from flask import Flask, request, jsonify
import json
import numpy as np
from pymongo import MongoClient
from pprint import pprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

home_model = joblib.load('home.joblib')
college_model = joblib.load('model.sav')
client = MongoClient("PUT_YOUR_CONNECTION_STRING_HERE")
db = client.its


watch_square = 's-02'
watch_xValue = 100
watch_yValue = -305


@app.route('/watch', methods=['POST'])
def watch():
    global watch_square, watch_xValue, watch_yValue

    request_object = json.loads(request.data)
    data_array = [0, 1, 2, 3, 4, 5, 6, 7]
    try:
        data_array[0] = request_object['AP-00']
        data_array[1] = request_object['AP-01']
        data_array[2] = request_object['AP-02']
        data_array[3] = request_object['AP-03']
        data_array[4] = request_object['AP-04']
        data_array[5] = request_object['AP-05']
        data_array[6] = request_object['AP-06']
        data_array[7] = request_object['AP-07']
    except KeyError as e:
        print()
        print(f'Message: {e} was not found...')
        print()
        return jsonify({'Message': f'{e} was not found...'})

    for i in range(len(data_array)):
        data_array[i] += 20

    matrix = np.array(data_array)
    matrix = matrix.reshape(1, -1)

    predicted_square = college_model.predict(matrix)[0]
    print(f'Watch Predicted Square: {predicted_square}')

    pixel_values = db.watch_squares.find_one(
        {'square': predicted_square})

    print(f'Pixel Values: {pixel_values}')
    del pixel_values['_id']

    watch_square = pixel_values['square']
    watch_xValue = pixel_values['xValue']
    watch_yValue = pixel_values['yValue']

    return jsonify({
        'status': 'success',
        'data': {
            'watch': {
                'square': watch_square,
                'xValue': watch_xValue,
                'yValue': watch_yValue
            },
        }
    }), 200


@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        try:
            request_object = json.loads(request.data)
            data_array = request_object['data']['values']

            matrix = np.array(data_array)
            matrix = matrix.reshape(1, -1)

            predicted_square = home_model.predict(matrix)[0]
            print(f'Predicted Square: {predicted_square}')

            pixel_values = db.squares.find_one(
                {'square': predicted_square})

            print(f'Pixel Values: {pixel_values}')
            del pixel_values['_id']

            return jsonify({
                'status': 'success',
                'data': {
                    'mobile': {
                        'square': pixel_values['square'],
                        'xValue': pixel_values['xValue'],
                        'yValue': pixel_values['yValue']
                    },
                    'watch': None
                }
            }), 200

        except:
            return jsonify({
                'message': 'Please make sure that you send a JSON object like the example attached to this response.',
                'status': 'failure'
            }), 400
    else:
        return jsonify({
            'status': 'failure',
            'message': 'this endpoint only accepts POST requests.'
        }), 405


@app.route('/mobile', methods=['POST'])
def mobile():
    global watch_square, watch_xValue, watch_yValue
    if request.method == 'POST':
        try:
            request_object = json.loads(request.data)
            data_array = request_object['data']['values']

            if len(data_array) < 8:
                return jsonify({'Status': 'failure', 'message': 'Some AP were missing'})

            for i in range(len(data_array)):
                data_array[i] += 20

            matrix = np.array(data_array)
            matrix = matrix.reshape(1, -1)

            predicted_square = college_model.predict(matrix)[0]
            print(f'Mobile Predicted Square: {predicted_square}')

            pixel_values = db.college_squares.find_one(
                {'square': predicted_square})

            del pixel_values['_id']

            return jsonify({
                'status': 'success',
                'data': {
                    'mobile': {
                        'square': pixel_values['square'],
                        'xValue': pixel_values['xValue'],
                        'yValue': pixel_values['yValue']
                    },
                    'watch': {
                        'square': watch_square,
                        'xValue': watch_xValue,
                        'yValue': watch_yValue
                    }
                }
            }), 200

        except:
            return jsonify({
                'message': 'Please make sure that you send a JSON object like the example attached to this response.',
                'status': 'failure'
            }), 400
    else:
        return jsonify({
            'status': 'failure',
            'message': 'this endpoint only accepts POST requests.'
        }), 405


if __name__ == '__main__':
    app.run(debug=True)
