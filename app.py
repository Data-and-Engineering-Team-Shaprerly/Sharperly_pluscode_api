from flask import Flask, request, jsonify
from pluscodes import openlocationcode

app = Flask(__name__)

def decode_plus_code(plus_code):
    coordinate = openlocationcode.decode(plus_code)
    return coordinate.latitudeCenter, coordinate.longitudeCenter

@app.route('/pluscode', methods=['POST'])
def get_lat_lon():
    data = request.json
    print(request.method)
    plus_code = data.get('plus_code')

    if not plus_code:
        return jsonify({'error': 'No Plus Code provided'}), 400

    try:
        lat, lon = decode_plus_code(plus_code)
        return jsonify({'latitude': lat, 'longitude': lon})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5050)