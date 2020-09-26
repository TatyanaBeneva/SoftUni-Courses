function smallestTwoNumbers(arrNum) {
    let result = arrNum.sort((a, b)=>a - b)
    .slice(0,2)
    .join(" ");
    console.log(result);
}

smallestTwoNumbers([30, 15, 50, 5]);
smallestTwoNumbers([0, 3, 10, 4, 7, 3]);