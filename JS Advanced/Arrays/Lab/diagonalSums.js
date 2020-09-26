function diagonalSums(input){
    let count = 0;
    let sumOfMain = 0;
    let sumOfSecondary = 0;
    const array = [];
    for(let i = 0; i < input.length; i++){
        sumOfMain += Number(input[i][count]);
        sumOfSecondary += Number(input[i][input[i].length - 1 - count]);
        count++;
    }
    
    array.push(sumOfMain, sumOfSecondary);
    console.log(array.join(' '));
}

diagonalSums([[20, 40],
    [10, 60]]
   );

diagonalSums([[3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]]
   );