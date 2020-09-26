function sumSub(array, startIndex, endIndex){
    try {
        if(typeof(array) !== 'object'){
            throw new TypeError('NaN');
        }
        
        if(startIndex < 0){
            startIndex = 0;
        }

        if(endIndex > array.length - 1){
            endIndex = array.length - 1;
        }
    } catch (error) {
        if(Number.isNaN(error)){
            return error.message;
        }
    }

    let sum = 0;

    for(let i = startIndex; i <= endIndex; i++){
        sum += Number(array[i]);
    }

    return sum;
}

console.log(sumSub('text', 0, 2));