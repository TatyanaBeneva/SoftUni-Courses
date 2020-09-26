function deleteByEmail() {
    let input = document.querySelector('input');
    let data = Array.from(document.querySelectorAll('tbody > tr'));
    let result = document.getElementById('result');
    var reg = /\w+@\w+.[a-z]{3}/;
    if(reg.test(input.value)){
        data.map(element =>{

            if(element.textContent.match(input.value, reg)){
                element.remove();
                result.textContent = 'Deleted.';
            }
        });
    }else{
        result.textContent = 'Not found.';       
    }

    input.value = '';

}