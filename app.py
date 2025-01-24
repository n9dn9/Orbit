from flask import Flask, request, jsonify
from flask_cors import CORS
from orbital import satellite_passes

app = Flask(__name__)
CORS(app)


@app.route('/satellite_passes', methods=['POST'])
def get_satellite_passes():
    data = request.json

    if not data:
        return "Информация не предоставлена", 400

    user_latitude = data.get('latitude')
    user_longitude = data.get('longitude')
    user_altitude = data.get('altitude', 0)
    user_station = data.get('station')

    if user_latitude is None or user_longitude is None or user_station is None:
        return "Не введена ширина и долгота", 400

    try:
        user_latitude = float(user_latitude)
        user_longitude = float(user_longitude)
        user_altitude = float(user_altitude)
    except ValueError:
        return "Ширина, долгота и высота должны быть числами", 400

    passes = satellite_passes(user_latitude, user_longitude, user_altitude, user_station)

    return jsonify(passes)
