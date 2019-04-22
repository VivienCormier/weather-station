import bme280_sensor
import ds18b20_therm
import tsl2561
import veml6075
import wind_direction
import wind

data = {
    'humidity': None,
    'pressure': None,
    'temperature': None,
    'lux': None,
    'uv_index': None,
    'uv_a': None,
    'uv_b': None,
    'wind_direction': None,
    'wind_gust': None,
    'wind_speed': None,
}

data.update(bme280_sensor.get_data())
data.update(ds18b20_therm.get_data())
data.update(tsl2561.get_data())
data.update(veml6075.get_data())
data.update(wind_direction.get_data())
data.update(wind.get_data())
print(data)
