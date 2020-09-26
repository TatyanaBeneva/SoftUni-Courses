function stopwatch() {
    let startBut = document.getElementById('startBtn')
    let stopBut = document.getElementById('stopBtn');
    let time = document.getElementById('time');
    let totalSec = 0;

    function pad(val){
        let valString = val + '';
        if(valString.length < 2){
            return '0' + valString;
        } else{
            return valString;
        }
    }
    let patern = (e) =>{
        let setTime = setInterval(function (){
            ++totalSec;
            time.innerHTML =pad(parseInt(totalSec / 60))  + ':' + pad(totalSec % 60);
        }, 1000);
        stopBut.disabled = false;
        startBut.setAttribute('disabled', true);

        stopBut.addEventListener('click', (e) =>{
            clearInterval(setTime);
            startBut.disabled = false;
            stopBut.disabled = true;
        })
    };
    startBut.addEventListener('click', patern);


}