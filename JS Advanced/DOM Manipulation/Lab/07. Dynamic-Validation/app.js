function validate() {
    let input = document.getElementById('email');
    var reg = /[a-z]+@[a-z]+.[a-z]+/;

    input.addEventListener('change', ()=> {
        if(!reg.test(input.value)){
            input.classList.add('error');
        }else{
            input.classList.remove('error');
        }
    });
}