(() => {
    const elements = {
        locationInput: document.querySelector('#location'),
        button: document.querySelector('#submit'),
        notificationHeading: document.querySelector('h1.notification'),
        currentDiv: document.querySelector('#current'),
        upcomingDiv: document.querySelector('#upcoming'),
        forecastWrapper: document.querySelector('#forecast')
    };

    const weatherSimbols = {
        "s": "☀",
        "p": "⛅",
        "o": "☁",
        "r": "☂",
        "d": "°"
    };

    const WEATHER_URL = "https://judgetests.firebaseio.com/forecast/{status}/{code}.json";
    const BASE_URL = "https://judgetests.firebaseio.com/locations.json";

    const errorHandler = (e) => {
        elements.notificationHeading.textContent = e.message;
    };

    const jsonMiddleware = (r) => r.json();

    elements.button.addEventListener('click', getLocationValue);

    function getLocationValue(){
        const location = elements.locationInput.value;

        fetch(BASE_URL)
            .then(jsonMiddleware)
            .then((data) => {
                const {name, code} = data.find(o => o.name === location);
                const CURRENT_TODAY_URL = WEATHER_URL.replace('{status}/{code}', `today/${code}`);
                const CURRENT_UPCOMING_URL = WEATHER_URL.replace('{status}/{code}', `upcoming/${code}`);

                Promise.all([
                    fetch(CURRENT_TODAY_URL).then(jsonMiddleware),
                    fetch(CURRENT_UPCOMING_URL).then(jsonMiddleware)
                ])
                .then(showWeatherLocation)
                .catch(errorHandler)
            })
            .catch(errorHandler);
    }

    function showWeatherLocation([todayData, upcomingData]){
        const {condition, high, low} = todayData.forecast;
        let forecastDiv = createHTMLElement('div', ['forecast']);
        let simbolSpan = createHTMLElement('span', ['condition', 'symbol'], weatherSimbols[condition[0].toLowerCase()]);
        let conditionSpan = createHTMLElement('span', ['condition']);
        let forecastFirstDataSpan = createHTMLElement('span', ['forecast-data'], todayData.name);
        let degreeseInfo = `${low}${weatherSimbols.d}/${high}${weatherSimbols.d}`;
        let forecastSecondDataSpan = createHTMLElement('span', ['forecast-data'],degreeseInfo);
        let forecastThirdDataSpan = createHTMLElement('span', ['forecast-data'], condition);

        conditionSpan.appendChild(forecastFirstDataSpan);
        conditionSpan.appendChild(forecastSecondDataSpan);
        conditionSpan.appendChild(forecastThirdDataSpan);
        forecastDiv.appendChild(simbolSpan);
        forecastDiv.appendChild(conditionSpan);
        elements.currentDiv.appendChild(forecastDiv);
        elements.forecastWrapper.style.display = "block";

        showUpcomingWeatherLocation(upcomingData);
        
    };

    function showUpcomingWeatherLocation({forecast, name}){
        let forecastInfoDiv = createHTMLElement('div', ['forecast-info']);

        forecast.forEach(({condition, high, low}) => {
            let upcomingSpan = createHTMLElement('span', ['upcoming']);
            let symbolSpan = createHTMLElement('span', ['symbol'], weatherSimbols[condition[0].toLowerCase()]);
            let degreeseInfo = `${low}${weatherSimbols.d}/${high}${weatherSimbols.d}`;
            let degreeseSpan = createHTMLElement('spna', ['forecast-data'], degreeseInfo);
            let conditionSpan = createHTMLElement('span', ['forecast-data'], condition);
            upcomingSpan.appendChild(symbolSpan);
            upcomingSpan.appendChild(degreeseSpan);
            upcomingSpan.appendChild(conditionSpan);
            forecastInfoDiv.appendChild(upcomingSpan);
        });

        elements.upcomingDiv.appendChild(forecastInfoDiv);
    }

    function createHTMLElement(tagName, className, textContent){
        let element = document.createElement(tagName);

        if(className){
            element.classList.add(...className);
        }

        if(textContent){
            element.textContent = textContent;
        }

        return element;
    }

})();