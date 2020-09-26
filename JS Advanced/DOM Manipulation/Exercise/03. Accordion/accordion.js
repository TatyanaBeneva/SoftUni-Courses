function toggle() {
    let button = document.getElementsByClassName('button')[0];
    let hiddingDiv = document.getElementById('extra');

    if(button.textContent === 'More'){
        button.textContent = 'Less';
        hiddingDiv.style.display = 'block';
    }else{
        button.textContent = 'More';
        hiddingDiv.style.display = 'none';
    }
}