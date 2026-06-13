"""
Global METAR Reader - Flask Application
Real-time airport weather decoder for 200+ worldwide airports
"""
from flask import Flask, render_template, request, jsonify
from metar_parser import parse_metar, parse_metar_structured
from airports import AIRPORTS, REGIONS

app = Flask(__name__)

# Airport data with METAR samples
SAMPLE_METARS = {code: metar for code, (city, country, metar) in AIRPORTS.items()}

def fetch_metar(airport_code):
    """Fetch or return sample METAR data"""
    airport_code = airport_code.upper()
    if airport_code in SAMPLE_METARS:
        return SAMPLE_METARS[airport_code]
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/metar', methods=['POST'])
def get_metar():
    code = request.json.get('airport_code', '') if request.json else ''
    if code is None:
        code = ''
    airport_code = str(code).strip().upper()

    if not airport_code or len(airport_code) < 2 or len(airport_code) > 4:
        return jsonify({'error': 'Please enter a valid airport code (e.g., KLAX)'}), 400

    metar_raw = fetch_metar(airport_code)
    if not metar_raw:
        return jsonify({'error': f'No METAR data found for {airport_code}. Check the airport code.'}), 404

    try:
        readable = parse_metar(metar_raw)
        details = parse_metar_structured(metar_raw)

        airport_info = AIRPORTS.get(airport_code, (airport_code, 'Unknown', ''))
        city, country = airport_info[0], airport_info[1]

        return jsonify({
            'airport_code': airport_code,
            'city': city,
            'country': country,
            'raw_metar': metar_raw,
            'readable': readable,
            'details': details
        })
    except Exception as e:
        return jsonify({'error': 'Failed to decode METAR data'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
