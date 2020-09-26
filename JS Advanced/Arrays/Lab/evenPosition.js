function evenPosition(inputArray){
    const array = [];
    for(let i = 0; i < inputArray.length; i++){
        if(i % 2 === 0){
            array.push(inputArray[i]);
        }
    }

    console.log(array.join(' '));
}

evenPosition(['20', '30', '40']);
evenPosition(['5', '10']);