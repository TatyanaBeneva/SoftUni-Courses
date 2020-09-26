function magicMatrices(input){
    let sum = 0;
    let result = true;
    for(let row = 0; row < input.length; row++){
        let rowSum = 0;
        let colSum = 0;
        for(let col = 0; col < input.length; col++){
            rowSum += input[row][col];
            colSum += input[col][row];
        }

        if(row === 0){
            sum = rowSum;
        }

        if(rowSum !== sum || colSum !== sum){
            result = false;
            break;
        }
    }

    console.log(result);
}

magicMatrices([[11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]]   
);