async function fetchMETAR() {
    const airportCode = document.getElementById('airportInput').value.trim().toUpperCase();
    const errorDiv = document.getElementById('error');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');

    errorDiv.style.display = 'none';
    resultDiv.style.display = 'none';
    errorDiv.textContent = '';

    if (!airportCode) {
        errorDiv.textContent = '✈️ Please enter an airport code';
        errorDiv.style.display = 'block';
        return;
    }

    if (airportCode.length < 2 || airportCode.length > 4) {
        errorDiv.textContent = '⚠️ Airport code must be 2-4 characters (e.g., KLAX)';
        errorDiv.style.display = 'block';
        return;
    }

    loadingDiv.style.display = 'flex';

    try {
        const response = await fetch('/api/metar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ airport_code: airportCode })
        });

        const data = await response.json();

        if (!response.ok) {
            errorDiv.textContent = '❌ ' + (data.error || 'Failed to fetch weather data');
            errorDiv.style.display = 'block';
            loadingDiv.style.display = 'none';
            return;
        }

        displayResults(data);
        loadingDiv.style.display = 'none';
        resultDiv.style.display = 'block';
        resultDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

    } catch (error) {
        errorDiv.textContent = '🌐 Network error. Please try again.';
        errorDiv.style.display = 'block';
        loadingDiv.style.display = 'none';
    }
}

function displayResults(data) {
    document.getElementById('resultAirport').textContent = data.airport_code;
    document.getElementById('resultCity').textContent = `${data.city}, ${data.country}`;
    document.getElementById('rawText').textContent = data.raw_metar;
    document.getElementById('readableText').textContent = data.readable;

    displayMainWeather(data.details);
    displayBreakdown(data.details);
    setWeatherIcon(data.readable);
}

function displayMainWeather(details) {
    document.getElementById('tempDisplay').textContent = details.temperature || '--°C';
    document.getElementById('windDisplay').textContent = details.wind || '--';
    document.getElementById('visibilityDisplay').textContent = details.visibility || '--';
}

function displayBreakdown(details) {
    const grid = document.getElementById('detailedBreakdown');
    grid.innerHTML = '';

    const items = [
        { label: 'Temperature', value: details.temperature },
        { label: 'Dew Point', value: details.dew_point },
        { label: 'Wind', value: details.wind },
        { label: 'Visibility', value: details.visibility },
        { label: 'Sky Conditions', value: details.sky_conditions },
        { label: 'Weather', value: details.weather },
        { label: 'Altimeter', value: details.altimeter },
        { label: 'Time', value: details.time }
    ];

    items.forEach(item => {
        if (item.value) {
            const div = document.createElement('div');
            div.className = 'breakdown-item';
            div.innerHTML = `<div class="breakdown-item-label">${item.label}</div><div class="breakdown-item-value">${item.value}</div>`;
            grid.appendChild(div);
        }
    });
}

function setWeatherIcon(readable) {
    const text = readable.toLowerCase();
    const icons = [
        { word: 'thunderstorm', icon: '⛈️' },
        { word: 'rain', icon: '🌧️' },
        { word: 'snow', icon: '❄️' },
        { word: 'fog', icon: '🌫️' },
        { word: 'mist', icon: '🌫️' },
        { word: 'overcast', icon: '☁️' },
        { word: 'broken', icon: '⛅' },
        { word: 'scattered', icon: '⛅' },
        { word: 'clear', icon: '☀️' },
        { word: 'excellent', icon: '☀️' },
        { word: 'few', icon: '🌤️' }
    ];

    let icon = '🌤️';
    for (const item of icons) {
        if (text.includes(item.word)) {
            icon = item.icon;
            break;
        }
    }
    document.getElementById('weatherIcon').textContent = icon;
}

function setAirport(code) {
    document.getElementById('airportInput').value = code;
    fetchMETAR();
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('airportInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') fetchMETAR();
    });
});
