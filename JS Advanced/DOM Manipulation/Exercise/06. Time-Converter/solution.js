function attachEventsListeners() {

    let daysBtn = document.getElementById('daysBtn');
    let hoursBtn = document.getElementById('hoursBtn');
    let minutesBtn = document.getElementById('minutesBtn');
    let secondsBtn = document.getElementById('secondsBtn');
    let inputDays = document.getElementById('days');
    let inputHours = document.getElementById('hours');
    let inputMinutes = document.getElementById('minutes');
    let inputSeconds = document.getElementById('seconds');

    daysBtn.addEventListener('click' ,(e) =>{
        let days = Number(inputDays.value);
        inputHours.value = days * 24;
        inputMinutes.value = days * 1440;
        inputSeconds.value = days * 86400;
    });

    hoursBtn.addEventListener('click', (e) =>{
        let hours = Number(inputHours.value);
        inputDays.value = hours / 24;
        inputMinutes.value = hours * 60;
        inputSeconds.value = hours * 3600;
    });

    minutesBtn.addEventListener('click', (e) =>{
        let minutes = Number(inputMinutes.value);
        inputDays.value = minutes / 1440;
        inputHours.value = minutes / 60;
        inputSeconds.value = minutes * 60;
    });

    secondsBtn.addEventListener('click', (e) =>{
        let seconds = Number(inputSeconds.value);
        inputDays.value = seconds / 86400;
        inputHours.value = seconds / 3600;
        inputMinutes.value = seconds / 60;
    })
}