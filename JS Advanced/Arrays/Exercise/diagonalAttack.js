function diagonalAttack(input){
    let array = input.map(x => x.split(' '));
    let leftSum = 0;
    let rightSum = 0;

    for(let i = 0; i < array.length; i++){
        leftSum += Number(array[i][i]);
        rightSum += Number(array[i][array.length - 1 - i]);
    }
        
    if(leftSum === rightSum){
        for(let i = 0; i < array.length; i++){
            for(let j = 0; j < array.length; j++){
                if(i !== j && i !== array.length - 1 - j){
                    array[i][j] = leftSum;
                }
            }
        }
    }

    array.forEach(element => {
        console.log(element.join(' '));
    });;
}
diagonalAttack(['6 3 12 3 1',
'11 4 23 2 5',
'101 12 3 21 10',
'1 4 5 2 2',
'5 22 33 11 1']
);