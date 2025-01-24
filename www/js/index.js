async function getPasses() {
    const button = document.getElementById('sumbit-button');
    const resultsContainer = document.getElementById('results');

    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const altitude = document.getElementById('altitude').value; 
    const stationList = document.getElementById('station');
    const station = stationList.options[stationList.selectedIndex].text; 

    const data = { latitude, longitude, altitude, station };

    buttonToggle(button, true, 'В процессе...');

    try {
        const response = await fetch('http://localhost:5000/satellite_passes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.text();
            throw new Error(errorData);
        }

        const result = await response.json();
        displayResults(result, resultsContainer);
        buttonToggle(button, false, 'Рассчитать');
    } catch (error) {
        buttonToggle(button, false, 'Рассчитать');
        alert(error.message)
    }
}

function buttonToggle(button, isDisabled, text) {
    button.disabled = isDisabled;
    button.innerText = text;
}

function displayResults(results, container) {
    container.innerHTML = '';
    results.forEach(satellite => {
        const satelliteDiv = document.createElement('div');
        satelliteDiv.className = 'satelite';
        satelliteDiv.innerHTML = `
            Время подъёма: ${satellite.rise_time}<br>
            Максимальное время: ${satellite.max_time}<br>
            Установленное время: ${satellite.set_time}
        `;
        container.appendChild(satelliteDiv);
    });
}
