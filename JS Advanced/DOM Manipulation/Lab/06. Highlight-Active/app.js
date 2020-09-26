function focus() {
    let inputs = document.querySelectorAll('div > input');
    let divs = document.querySelectorAll('div');

    for(let i = 0; i < inputs.length; i++){
        let div = inputs[i].parentElement;
        inputs[i].addEventListener('focus', (e) =>{
            divs.forEach(el => {
                if(el.classList.contains('focused')){
                    el.classList.remove('focused');
                }
            })

            div.classList.add('focused');
        })
    }

    
}