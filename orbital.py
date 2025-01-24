from pyorbital.orbital import Orbital
import datetime


def satellite_passes(latitude, longitude, altitude, station):
    orb = Orbital(station)
    start_time = datetime.datetime.utcnow()
    end_time = start_time + datetime.timedelta(days=3)

    length = int((end_time - start_time).total_seconds() / 3600)
    passes = orb.get_next_passes(start_time, length, latitude, longitude, altitude)
    response = []

    for pass_info in passes:
        rise_time, max_time, set_time = pass_info
        max_altitude = orb.get_observer_look(max_time, latitude, longitude, altitude)[1]

        pass_data = {
            'rise_time': rise_time.isoformat(),
            'max_time': max_time.isoformat(),
            'set_time': set_time.isoformat(),
            'max_altitude': max_altitude
        }

        if max_altitude > 10:
            trajectory = []
            current_time = rise_time
            while current_time <= set_time:
                az, el = orb.get_observer_look(current_time, latitude, longitude, altitude)
                trajectory.append({
                    'time': current_time.isoformat(),
                    'azimuth': az,
                    'elevation': el
                })
                current_time += datetime.timedelta(seconds=10)

            pass_data['trajectory'] = trajectory

        response.append(pass_data)

    return response
