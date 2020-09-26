function orbit(data){
    const array = [];
    let rowIndex = Number(data[0]);
    let colIndex = Number(data[1]);
    let rowCordinate = Number(data[2]);
    let colCordinate = Number(data[3]);

    for(let row = 0; row < rowIndex; row++){
        let rowArray = [];

        for(let col = 0; col < colIndex; col++){
            
            rowArray[col] = Math.max(Math.abs(row - rowCordinate), Math.abs(col - colCordinate)) + 1;
        }
        array.push(rowArray);
    }

    array.forEach(element => {
        console.log(element.join(' '));
    });
}

orbit([4, 4, 0, 0]);