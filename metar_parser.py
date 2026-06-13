import re
from datetime import datetime

def _parse_metar_parts(metar_string):
    """Internal helper: Parse METAR parts into structured dict"""
    parts = metar_string.split()
    if not parts:
        return {}

    result = {
        'time': '',
        'wind': '',
        'visibility': '',
        'weather': '',
        'temperature': '',
        'dew_point': '',
        'altimeter': '',
        'sky_conditions': ''
    }

    i = 1
    while i < len(parts):
        part = parts[i]
        if i == 1 and part.endswith('Z'):
            result['time'] = parse_time(part)
        elif 'KT' in part or 'MPS' in part:
            result['wind'] = parse_wind(part)
        elif 'SM' in part:
            result['visibility'] = parse_visibility(part)
        elif part.startswith('R') and 'FT' in part:
            pass
        elif is_weather(part):
            result['weather'] = parse_weather(part)
        elif is_sky_condition(part):
            result['sky_conditions'] = parse_sky(part)
        elif is_temp_dew(part):
            temp, dew = parse_temp_dew(part)
            result['temperature'] = temp
            result['dew_point'] = dew
        elif (part.startswith('A') or part.startswith('Q')) and len(part) == 5 and part[1:].isdigit():
            result['altimeter'] = parse_altimeter(part) if part.startswith('A') else parse_altimeter_metric(part)
        elif part == 'RMK':
            break
        i += 1

    return result

def parse_metar_structured(metar_string):
    """Parse METAR and return structured dict with all details"""
    result = _parse_metar_parts(metar_string)
    return {k: v for k, v in result.items() if v}

def parse_metar(metar_string):
    """Parse METAR string and return plain English description"""
    parts = metar_string.split()
    if not parts:
        return "Invalid METAR data"

    result = _parse_metar_parts(metar_string)
    return format_readable(result)

def parse_time(time_str):
    """Parse time like 121853Z"""
    if not time_str or len(time_str) < 6:
        return ""
    day = time_str[:2]
    hour = time_str[2:4]
    minute = time_str[4:6]
    return f"{day}th day at {hour}:{minute} UTC"

def parse_wind(wind_str):
    """Parse wind like 26008KT or VRB03KT"""
    if 'VRB' in wind_str:
        speed = wind_str[3:5]
        return f"Variable wind {speed} knots"

    direction = wind_str[:3]
    speed = wind_str[3:5]
    gust = ""

    if 'G' in wind_str:
        parts = wind_str.replace('KT', '').replace('MPS', '').split('G')
        speed = parts[0][3:5]
        gust_speed = parts[1]
        gust = f", gusting to {gust_speed} knots"

    try:
        dir_int = int(direction)
        dir_name = direction_to_name(dir_int)
        return f"Wind from {dir_name} ({direction}°) at {speed} knots{gust}"
    except:
        return f"Wind {wind_str}"

def direction_to_name(degrees):
    """Convert wind direction degrees to compass direction"""
    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    idx = round(degrees / 22.5) % 16
    return directions[idx]

def parse_visibility(vis_str):
    """Parse visibility like 10SM or 1/2SM"""
    vis_str = vis_str.replace('SM', '')
    if vis_str == '10':
        return "Visibility 10+ miles (excellent)"
    elif vis_str == 'P6':
        return "Visibility greater than 6 statute miles (excellent)"
    else:
        return f"Visibility {vis_str} miles"

def parse_weather(weather_str):
    """Parse weather phenomena like -RA, +TSRA"""
    descriptions = {
        'RA': 'rain',
        'SN': 'snow',
        'SG': 'snow grains',
        'IC': 'ice crystals',
        'PL': 'ice pellets',
        'GR': 'hail',
        'GS': 'small hail',
        'UP': 'unidentified precipitation',
        'BR': 'mist',
        'FG': 'fog',
        'FU': 'smoke',
        'VA': 'volcanic ash',
        'DU': 'dust',
        'SA': 'sand',
        'HZ': 'haze',
        'PY': 'spray',
        'TS': 'thunderstorm',
        'SQ': 'squall',
        'FC': 'funnel cloud',
        'SS': 'sandstorm',
        'DS': 'dust storm'
    }

    intensity = ""
    if weather_str.startswith('-'):
        intensity = "light "
        weather_str = weather_str[1:]
    elif weather_str.startswith('+'):
        intensity = "heavy "
        weather_str = weather_str[1:]

    phenomena = []
    i = 0
    while i < len(weather_str):
        for code, desc in descriptions.items():
            if weather_str[i:].startswith(code):
                phenomena.append(desc)
                i += len(code)
                break
        else:
            i += 1

    if phenomena:
        return intensity + ", ".join(phenomena)
    return ""

def is_weather(part):
    """Check if part is weather phenomena"""
    weather_codes = ['RA', 'SN', 'SG', 'IC', 'PL', 'GR', 'GS', 'UP', 'BR', 'FG',
                     'FU', 'VA', 'DU', 'SA', 'HZ', 'PY', 'TS', 'SQ', 'FC', 'SS', 'DS', 'MIST']
    return any(code in part for code in weather_codes)

def parse_sky(sky_str):
    """Parse sky conditions like FEW250, BKN100"""
    coverage_map = {
        'SKC': 'Sky clear',
        'CLR': 'Clear',
        'FEW': 'Few clouds',
        'SCT': 'Scattered clouds',
        'BKN': 'Broken cloud cover',
        'OVC': 'Overcast'
    }

    for code, description in coverage_map.items():
        if sky_str.startswith(code):
            altitude = sky_str[len(code):]
            if altitude and altitude.isdigit():
                feet = int(altitude) * 100
                return f"{description} at {feet} feet"
            return description

    return ""

def is_sky_condition(part):
    """Check if part is sky condition"""
    return any(part.startswith(code) for code in ['SKC', 'CLR', 'FEW', 'SCT', 'BKN', 'OVC'])

def is_temp_dew(part):
    """Check if part is temperature/dew point"""
    return '/' in part and any(c.isdigit() for c in part)

def parse_temp_dew(temp_str):
    """Parse temperature/dew point like 23/14 or M05/M10"""
    parts = temp_str.split('/')
    if len(parts) != 2:
        return "", ""

    temp = parse_temperature(parts[0])
    dew = parse_temperature(parts[1])
    return temp, dew

def parse_temperature(temp_str):
    """Parse single temperature value"""
    if not temp_str:
        return ""
    if temp_str.startswith('M'):
        celsius = -int(temp_str[1:])
    else:
        celsius = int(temp_str)

    fahrenheit = round((celsius * 9/5) + 32)
    return f"{celsius}°C ({fahrenheit}°F)"

def parse_altimeter(alt_str):
    """Parse altimeter like A3012"""
    if len(alt_str) < 5:
        return ""
    inches = alt_str[1:3] + '.' + alt_str[3:5]
    return f"Altimeter {inches} inHg"

def parse_altimeter_metric(alt_str):
    """Parse altimeter like Q1020"""
    if len(alt_str) < 5:
        return ""
    hectopascals = alt_str[1:]
    return f"Altimeter {hectopascals} hPa"

def format_readable(result):
    """Format parsed METAR into readable text"""
    parts = []

    if result['sky_conditions']:
        parts.append(result['sky_conditions'])

    if result['weather']:
        parts.append(result['weather'])

    if result['temperature']:
        parts.append(result['temperature'])

    if result['wind']:
        parts.append(result['wind'])

    if result['visibility']:
        parts.append(result['visibility'])

    if result['altimeter']:
        parts.append(result['altimeter'])

    readable = ". ".join(parts)
    if readable:
        readable += "."

    return readable if readable else "Unable to decode METAR"
