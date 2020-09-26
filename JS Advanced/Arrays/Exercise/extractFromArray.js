function extractFromArray(input){
    let first = Number.NEGATIVE_INFINITY;
    for(let i = 0; i < input.length; i++){
        if(input[i] >= first){
            first = input[i]
            console.log(first);            
        }
    }
}

extractFromArray([1, 
    3, 
    8, 
    4, 
    10, 
    12, 
    3, 
    2, 
    24]
    );