
function negativePositive(input){
    const result = [];

    for(let i = 0; i < input.length; i++){
        let number = Number(input[i]);

        if(number < 0){
            result.splice(0,0,number);
        }else{
            result.push(number);
        }
    }

    result.forEach(element => {
        console.log(element);
    })
}

negativePositive([7, -2, 8, 9]);
negativePositive([3, -2, 0, -1]);

