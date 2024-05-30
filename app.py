from flask import Flask, request, jsonify, render_template
from pluscodes import openlocationcode

app = Flask(__name__)

def decode_plus_code(plus_code):
    coordinate = openlocationcode.decode(plus_code)
    return coordinate.latitudeCenter, coordinate.longitudeCenter

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/pluscode', methods=['GET', 'POST'])
def get_lat_lon():
    if request.method == 'POST':
        data = request.form
        plus_code = data.get('plus_code')
        if not plus_code:
            return jsonify({'error': 'No Plus Code provided'}), 400

        try:
            lat, lon = decode_plus_code(plus_code)
            return jsonify({'latitude': lat, 'longitude': lon})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Please submit a POST request with a Plus Code.'})

# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=10000)
