"""
Unit tests for Global METAR Reader
Tests: Flask app, METAR parser, API endpoints, and global airport coverage
"""
import pytest
import json
from app import app, SAMPLE_METARS
from metar_parser import parse_metar
from airports import AIRPORTS, REGIONS


@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestMETARParser:
    """Test METAR decoding functionality"""

    def test_parse_temperature(self):
        """Test temperature parsing and C-to-F conversion"""
        metar = "TEST 121900Z 18010KT 10SM FEW100 20/15 A3000"
        result = parse_metar(metar)
        assert '20°C' in result
        assert '68°F' in result

    def test_parse_negative_temperature(self):
        """Test parsing negative temperatures"""
        metar = "TEST 121900Z 18010KT 10SM FEW100 M05/M10 Q1010"
        result = parse_metar(metar)
        assert '-5°C' in result
        assert '23°F' in result

    def test_parse_wind_with_gusts(self):
        """Test wind parsing with gust information"""
        metar = "TEST 121900Z 31015G25KT 9999 BKN040 12/08 Q1012"
        result = parse_metar(metar)
        assert 'Wind' in result
        assert 'gusting to 25' in result

    def test_parse_visibility(self):
        """Test visibility parsing"""
        metar = "TEST 121900Z 18010KT 10SM FEW100 20/15 A3000"
        result = parse_metar(metar)
        assert '10+ miles' in result.lower() or 'visibility' in result.lower()

    def test_parse_weather_phenomena(self):
        """Test weather phenomena parsing (rain, snow, etc.)"""
        metar = "TEST 121900Z 18010KT 4SM -RA BR BKN025 14/12 A3000"
        result = parse_metar(metar)
        assert 'mist' in result.lower()

    def test_parse_sky_conditions(self):
        """Test cloud coverage and altitude parsing"""
        metar = "TEST 121900Z 18010KT 10SM OVC050 15/10 A3000"
        result = parse_metar(metar)
        assert 'Overcast' in result


class TestFlaskApp:
    """Test Flask application routes and functionality"""

    def test_home_page_loads(self, client):
        """Test home page loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Global METAR Reader' in response.data

    def test_home_page_has_search(self, client):
        """Test home page has search functionality"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'airportInput' in response.data

    def test_home_page_has_region_tabs(self, client):
        """Test home page displays region tabs"""
        response = client.get('/')
        assert response.status_code == 200
        # Check for region indicators
        regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']
        for region in regions:
            assert region.encode() in response.data or region.split()[0].encode() in response.data


class TestMetarAPI:
    """Test METAR API endpoints"""

    def test_api_successful_query(self, client):
        """Test API returns weather data for valid airport"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'EGLL'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['airport_code'] == 'EGLL'
        assert 'raw_metar' in data
        assert 'readable' in data
        assert 'city' in data
        assert 'country' in data

    def test_api_returns_airport_details(self, client):
        """Test API returns complete airport information"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'RJTT'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['city'] == 'Tokyo Haneda'
        assert data['country'] == 'Japan'

    def test_api_case_insensitive(self, client):
        """Test API handles lowercase airport codes"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'egll'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['airport_code'] == 'EGLL'

    def test_api_empty_code_error(self, client):
        """Test API validation for empty airport code"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': ''}),
                              content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data

    def test_api_invalid_code_error(self, client):
        """Test API returns error for invalid airport code"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'XXXX'}),
                              content_type='application/json')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data

    def test_api_short_code_error(self, client):
        """Test API validation for too-short airport code"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'K'}),
                              content_type='application/json')
        assert response.status_code == 400


class TestGlobalAirportCoverage:
    """Test coverage of major airports worldwide"""

    def test_total_airports_available(self):
        """Test that comprehensive airport database is loaded"""
        assert len(AIRPORTS) >= 100, f"Should have 100+ airports, got {len(AIRPORTS)}"

    def test_all_regions_present(self):
        """Test all major regions are represented"""
        expected_regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']
        for region in expected_regions:
            assert region in REGIONS, f"Missing region: {region}"

    def test_uk_airports(self, client):
        """Test UK airports coverage"""
        uk_airports = ['EGLL', 'EGKK', 'EGSS', 'EGPN', 'EGCC', 'EGPH']
        for airport in uk_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_usa_airports(self, client):
        """Test USA airports coverage"""
        usa_airports = ['KLAX', 'KJFK', 'KSFO', 'KORD', 'KDFW']
        for airport in usa_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_europe_airports(self, client):
        """Test European airports coverage"""
        eu_airports = ['LFPG', 'EDDF', 'LEMD', 'LIRF', 'LHBP']
        for airport in eu_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_asia_airports(self, client):
        """Test Asian airports coverage"""
        asia_airports = ['RJTT', 'ZBAA', 'VHHH', 'VIDP', 'WSSS']
        for airport in asia_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_australia_airports(self, client):
        """Test Australian airports coverage"""
        au_airports = ['YSSY', 'YMML', 'YBBN']
        for airport in au_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_south_america_airports(self, client):
        """Test South American airports coverage"""
        sa_airports = ['SBGR', 'SABE', 'SCEL']
        for airport in sa_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_africa_airports(self, client):
        """Test African airports coverage"""
        af_airports = ['FAOR', 'HECA', 'DIAP']
        for airport in af_airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200


class TestMetarDataQuality:
    """Test quality and consistency of METAR data"""

    def test_all_airports_have_metar(self):
        """Test all airports have valid METAR samples"""
        for code, (city, country, metar) in AIRPORTS.items():
            assert isinstance(code, str), f"Code must be string: {code}"
            assert isinstance(city, str), f"City must be string: {city}"
            assert isinstance(country, str), f"Country must be string: {country}"
            assert isinstance(metar, str), f"METAR must be string: {metar}"
            assert len(metar) > 10, f"METAR too short for {code}"

    def test_sample_metars_match_airports(self):
        """Test SAMPLE_METARS keys match AIRPORTS"""
        assert set(SAMPLE_METARS.keys()) == set(AIRPORTS.keys())

    def test_regions_reference_valid_airports(self):
        """Test region mappings reference only valid airports"""
        all_codes = set(AIRPORTS.keys())
        for region, countries in REGIONS.items():
            for country, codes in countries.items():
                for code in codes:
                    assert code in all_codes, f"{code} in {region}/{country} not in AIRPORTS"


class TestAPIResponseFormat:
    """Test API response format and structure"""

    def test_response_has_required_fields(self, client):
        """Test API response includes all required fields"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KLAX'}),
                              content_type='application/json')
        data = json.loads(response.data)
        required_fields = ['airport_code', 'city', 'country', 'raw_metar', 'readable', 'details']
        for field in required_fields:
            assert field in data, f"Missing field: {field}"

    def test_response_readable_is_non_empty(self, client):
        """Test readable weather report is populated"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'EGLL'}),
                              content_type='application/json')
        data = json.loads(response.data)
        assert len(data['readable']) > 20
        assert isinstance(data['readable'], str)

    def test_error_response_format(self, client):
        """Test error responses have consistent format"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'INVALID'}),
                              content_type='application/json')
        data = json.loads(response.data)
        assert 'error' in data
        assert isinstance(data['error'], str)


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_airport_code_max_length(self, client):
        """Test airport code at maximum length (4 chars)"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KJFK'}),
                              content_type='application/json')
        assert response.status_code == 200

    def test_airport_code_min_length(self, client):
        """Test airport code at minimum length (2 chars)"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'LA'}),
                              content_type='application/json')
        assert response.status_code in [200, 404]

    def test_airport_code_with_spaces(self, client):
        """Test airport code with surrounding spaces (should be trimmed)"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': '  KLAX  '}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['airport_code'] == 'KLAX'

    def test_airport_code_mixed_case(self, client):
        """Test airport code with mixed case"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KlAx'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['airport_code'] == 'KLAX'

    def test_empty_json_body(self, client):
        """Test API with empty JSON body"""
        response = client.post('/api/metar',
                              data=json.dumps({}),
                              content_type='application/json')
        assert response.status_code == 400

    def test_missing_airport_code_field(self, client):
        """Test API with missing airport_code field"""
        response = client.post('/api/metar',
                              data=json.dumps({'city': 'Los Angeles'}),
                              content_type='application/json')
        assert response.status_code == 400

    def test_null_airport_code(self, client):
        """Test API with null airport code"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': None}),
                              content_type='application/json')
        assert response.status_code == 400

    def test_numeric_airport_code(self, client):
        """Test airport code with only numbers"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': '1234'}),
                              content_type='application/json')
        assert response.status_code == 404

    def test_special_characters_in_code(self, client):
        """Test airport code with special characters"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KLA@'}),
                              content_type='application/json')
        assert response.status_code == 404

    def test_very_long_airport_code(self, client):
        """Test airport code exceeding max length"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KLAXABCD'}),
                              content_type='application/json')
        assert response.status_code == 400


class TestFlaskWebRoutes:
    """Test all Flask routes and web endpoints"""

    def test_home_route_get(self, client):
        """Test GET / route"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'<!DOCTYPE html>' in response.data

    def test_home_route_content_type(self, client):
        """Test home page returns HTML content type"""
        response = client.get('/')
        assert 'text/html' in response.content_type

    def test_api_metar_post_only(self, client):
        """Test /api/metar only accepts POST"""
        response = client.get('/api/metar')
        assert response.status_code in [405, 404]

    def test_invalid_route(self, client):
        """Test accessing non-existent route"""
        response = client.get('/invalid/route')
        assert response.status_code == 404

    def test_api_metar_requires_json(self, client):
        """Test API requires JSON content type"""
        response = client.post('/api/metar',
                              data='airport_code=KLAX',
                              content_type='application/x-www-form-urlencoded')
        assert response.status_code in [400, 415]

    def test_home_page_includes_title(self, client):
        """Test home page has proper title"""
        response = client.get('/')
        assert b'Global METAR Reader' in response.data

    def test_home_page_has_airports_script(self, client):
        """Test home page includes JavaScript for airports"""
        response = client.get('/')
        assert b'script' in response.data.lower()


class TestMETARIntegration:
    """Test complete METAR decoding integration"""

    def test_complete_metar_flow_klax(self, client):
        """Test complete flow: search KLAX and verify all data"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KLAX'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)

        assert data['airport_code'] == 'KLAX'
        assert data['city'] == 'Los Angeles'
        assert data['country'] == 'USA'
        assert len(data['raw_metar']) > 15
        assert len(data['readable']) > 20
        assert '°C' in data['readable'] or '°F' in data['readable']

    def test_complete_metar_flow_egll(self, client):
        """Test complete flow: search EGLL and verify all data"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'EGLL'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)

        assert data['airport_code'] == 'EGLL'
        assert data['city'] == 'London Heathrow'
        assert data['country'] == 'UK'
        assert 'Wind' in data['readable']

    def test_complete_metar_flow_rjtt(self, client):
        """Test complete flow: search RJTT and verify all data"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'RJTT'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)

        assert data['airport_code'] == 'RJTT'
        assert data['city'] == 'Tokyo Haneda'
        assert data['country'] == 'Japan'

    def test_metar_details_contain_all_fields(self, client):
        """Test that METAR details include all parsed fields"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'EGLL'}),
                              content_type='application/json')
        data = json.loads(response.data)
        details = data['details']

        assert isinstance(details, dict)
        assert len(details) > 0
        assert any(k in details for k in ['temperature', 'wind', 'visibility', 'sky_conditions', 'altimeter'])

    def test_metar_readable_matches_details(self, client):
        """Test that readable text contains info from details"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KLAX'}),
                              content_type='application/json')
        data = json.loads(response.data)

        readable = data['readable'].lower()
        if 'temperature' in data['details']:
            assert '°c' in readable or '°f' in readable
        if 'wind' in data['details']:
            assert 'wind' in readable or 'knot' in readable

    def test_metar_response_json_valid(self, client):
        """Test that API response is valid JSON"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'YSSY'}),
                              content_type='application/json')
        assert response.status_code == 200
        try:
            data = json.loads(response.data)
            assert isinstance(data, dict)
        except json.JSONDecodeError:
            pytest.fail("API response is not valid JSON")

    def test_multiple_airport_queries(self, client):
        """Test querying multiple airports in sequence"""
        airports = ['KLAX', 'EGLL', 'RJTT', 'YSSY']
        for airport in airports:
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': airport}),
                                  content_type='application/json')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['airport_code'] == airport


class TestAPINetworkErrors:
    """Test API resilience and error handling"""

    def test_malformed_json(self, client):
        """Test API with malformed JSON"""
        response = client.post('/api/metar',
                              data='{invalid json}',
                              content_type='application/json')
        assert response.status_code in [400, 415]

    def test_missing_content_type(self, client):
        """Test API request without content type"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'KLAX'}))
        assert response.status_code in [200, 400, 415]

    def test_very_large_json_body(self, client):
        """Test API with very large JSON body"""
        large_data = {'airport_code': 'KLAX', 'extra': 'x' * 10000}
        response = client.post('/api/metar',
                              data=json.dumps(large_data),
                              content_type='application/json')
        assert response.status_code in [200, 400, 413]

    def test_error_response_is_json(self, client):
        """Test that error responses are valid JSON"""
        response = client.post('/api/metar',
                              data=json.dumps({'airport_code': 'XXXX'}),
                              content_type='application/json')
        assert response.status_code == 404
        try:
            data = json.loads(response.data)
            assert 'error' in data
        except json.JSONDecodeError:
            pytest.fail("Error response is not valid JSON")

    def test_consecutive_requests(self, client):
        """Test multiple consecutive API requests"""
        for i in range(5):
            response = client.post('/api/metar',
                                  data=json.dumps({'airport_code': 'KLAX'}),
                                  content_type='application/json')
            assert response.status_code == 200

    def test_interleaved_valid_invalid_requests(self, client):
        """Test alternating valid and invalid requests"""
        valid = {'airport_code': 'KLAX'}
        invalid = {'airport_code': 'XXXX'}

        response1 = client.post('/api/metar', data=json.dumps(valid), content_type='application/json')
        assert response1.status_code == 200

        response2 = client.post('/api/metar', data=json.dumps(invalid), content_type='application/json')
        assert response2.status_code == 404

        response3 = client.post('/api/metar', data=json.dumps(valid), content_type='application/json')
        assert response3.status_code == 200
