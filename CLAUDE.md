# CLAUDE.md

Development guide for Global METAR Reader - Flask application for decoding airport weather reports.

## Setup & Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install development dependencies  
pip install -e ".[dev]"
```

## Running the Application

```bash
# Start Flask development server
python3 app.py

# Server runs on http://localhost:8000
```

## Running Tests

```bash
# Run all 60 tests
pytest test_metar_reader.py -v

# Run with coverage report
pytest test_metar_reader.py --cov=metar_parser --cov=app --cov-report=term-missing

# Run specific test class
pytest test_metar_reader.py::TestMETARParser -v

# Run edge cases and integration tests
pytest test_metar_reader.py::TestEdgeCases -v
pytest test_metar_reader.py::TestMETARIntegration -v

# Run network resilience tests
pytest test_metar_reader.py::TestAPINetworkErrors -v

# Quick test run
pytest test_metar_reader.py -q
```

## Project Structure

```
METAR-READER/
├── app.py                      Flask application entry point
├── metar_parser.py             METAR decoding logic (168 lines)
├── airports.py                 Airport database: 117 airports across 50+ countries
├── requirements.txt            Python dependencies
├── test_metar_reader.py        30 comprehensive unit tests
├── README.md                   User documentation
├── CONTRIBUTING.md             Contribution guidelines
├── templates/
│   └── index.html              Web interface
├── static/
│   ├── style.css               Styling (modern gradient design)
│   └── script.js               Frontend logic
└── CLAUDE.md                   This file
```

## Code Architecture

### `app.py` (Flask Application)
- Serves web interface and API
- Route: `GET /` — HTML page with airport browser
- Route: `POST /api/metar` — JSON API for weather queries
- Returns: airport code, city, country, raw METAR, readable report

### `metar_parser.py` (Core METAR Decoder)
- Parses standardized METAR format into plain English
- Handles: temperature, wind, visibility, clouds, weather phenomena, altimeter
- Converts Celsius to Fahrenheit
- Supports compass directions (N, NE, E, SE, S, SW, W, NW)
- 90%+ test coverage

### `airports.py` (Database)
- 117 major airports from 50+ countries
- Data structure: `ICAO code → (City, Country, Sample METAR)`
- Organized by 6 regions: North America, South America, Europe, Asia, Africa, Oceania
- Each airport has realistic sample METAR data for testing

### Frontend (`templates/` & `static/`)
- Modern gradient UI with tab-based airport browser
- Real-time decoding with emoji weather icons
- Responsive design for mobile/desktop
- Search by airport code or browse by country

## Key Dependencies

- **Flask 2.3.3** — Web framework
- **Requests 2.31.0** — HTTP library (optional, for future real API integration)
- **pytest 7.4.0** — Testing framework (dev only)
- **pytest-cov 4.1.0** — Coverage reporting (dev only)

## Testing Philosophy

- **60 comprehensive tests** across 9 test classes
- Focus on behavior, edge cases, and integration
- Test classes: Parser, Flask routes, API, edge cases, integration, network resilience, global coverage, data quality, response format
- Each test is self-contained and independent
- 94% code coverage across core modules
- Tests cover:
  - **Parser Logic** — temperature, wind, visibility, weather phenomena, sky conditions
  - **API Endpoints** — validation, error handling, response format
  - **Edge Cases** — null values, overflow, special characters, boundary conditions
  - **Integration** — complete METAR flows, multi-query sequences
  - **Network Resilience** — malformed JSON, large payloads, consecutive requests
  - **Web Routes** — GET/POST validation, content types, 404 handling
  - **Global Coverage** — 117 airports, 6 regions, per-continent validation
  - **Data Quality** — METAR validity, database consistency

## Test Classes Reference

| Class | Tests | Purpose |
|---|---|---|
| `TestMETARParser` | 6 | Core decoder functionality (temperature, wind, visibility, weather, clouds) |
| `TestFlaskApp` | 3 | Web interface routes and content |
| `TestMetarAPI` | 6 | API endpoint validation and error handling |
| `TestGlobalAirportCoverage` | 9 | Database completeness (100+ airports, 6 regions, per-continent) |
| `TestMetarDataQuality` | 3 | Data consistency and validity |
| `TestAPIResponseFormat` | 4 | Response field validation and JSON structure |
| `TestEdgeCases` | 10 | Boundary conditions, null values, overflow, special characters |
| `TestFlaskWebRoutes` | 7 | HTTP methods, content types, routing |
| `TestMETARIntegration` | 7 | End-to-end flows, multi-query sequences |
| `TestAPINetworkErrors` | 6 | Malformed JSON, large payloads, network resilience |

**Running specific test classes:**
```bash
pytest test_metar_reader.py::TestEdgeCases -v
pytest test_metar_reader.py::TestMETARIntegration -v
pytest test_metar_reader.py::TestAPINetworkErrors -v
```

## Development Best Practices

1. **No External Dependencies at Runtime** — Flask + Requests only, no heavy libs
2. **Type Hints** — Functions annotated for clarity (Python 3.8+)
3. **Docstrings** — All public functions documented with examples
4. **Test-Driven** — Add tests before modifying METAR parser
5. **No Code Duplication** — Single airports.py file, one parser implementation
6. **Simple Error Handling** — Validate at boundaries (user input), trust internal code

## API Usage

```bash
# Request
curl -X POST http://localhost:8000/api/metar \
  -H "Content-Type: application/json" \
  -d '{"airport_code": "EGLL"}'

# Response (Full Example)
{
  "airport_code": "EGLL",
  "city": "London Heathrow",
  "country": "UK",
  "raw_metar": "EGLL 121850Z 31015G25KT 9999 BKN040 OVC080 12/08 Q1012",
  "readable": "Overcast at 8000 feet. 12°C (54°F). Wind from NW (310°) at 15 knots, gusting to 25 knots. Visibility 10+ miles. Altimeter 1012 hPa.",
  "details": {
    "temperature": "12°C (54°F)",
    "dew_point": "8°C (46°F)",
    "wind": "Wind from NW (310°) at 15 knots, gusting to 25 knots",
    "visibility": "Visibility 10+ miles (excellent)",
    "sky_conditions": "Overcast at 8000 feet",
    "altimeter": "Altimeter 1012 hPa",
    "time": "12th day at 18:50 UTC"
  }
}
```

**Response Fields:**
- `airport_code` — ICAO code (uppercase)
- `city` — City name
- `country` — Country name
- `raw_metar` — Original METAR string
- `readable` — Plain English summary
- `details` — Structured breakdown of all weather parameters

## Extending the Database

To add airports:
1. Add entry to `AIRPORTS` dict in `airports.py`: `'XXXX': ('City', 'Country', 'METAR sample')`
2. Add code reference to appropriate `REGIONS` sub-dict
3. Update test count in `test_metar_reader.py` if needed
4. Run `pytest` to verify

## Deployment

### Local Development
```bash
python3 app.py
```

### Production (Flask + Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker (Optional Future)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]
```

## Performance Notes

- No database queries — all data in-memory
- METAR parsing is O(n) in string length, typically <1ms per decode
- Web server handles 100+ concurrent connections easily
- CSS/JS files cached in browser

## Future Improvements

- Real-time METAR fetching from aviation APIs (Aviation Weather Center, AVWX)
- Historical weather data
- Weather alerts & warnings
- Multi-language support
- Mobile app (React Native)
- Automated airport database updates

## Publishing to PyPI (Optional)

```bash
# Build distribution
python3 -m build

# Upload to PyPI
twine upload dist/*
```

Then users can `pip install metar-reader`.
