function biggestElement(input){
    let number = 0;
    let biggestNum = Number.NEGATIVE_INFINITY;
    input.forEach(item => {
        number = item.reduce((a,b) => a < b ? b : a, Number.NEGATIVE_INFINITY);

        if(number > biggestNum){
            biggestNum = number;
        }
    });

    console.log(biggestNum);
}

biggestElement([[20, 50, 10],
    [8, 33, 145]]
   );