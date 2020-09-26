function ticTacToe(input){
    const array = [[false, false, false],
    [false, false, false],
    [false, false, false]];
    let player = 'X';
    const moves = [];
    for(let i = 0; i < input.length; i++){
        moves[i] = input[i].split(' ');    
    }

    for(let i = 0; i < moves.length; i++){
        let row = Number(moves[i][0]);
        let col = Number(moves[i][1]);
        if(player === 'X'){
            if(array[row][col] === false){
                array[row].splice(col, 1, 'X');
                player = 'O';
            }else{
                console.log('This place is already taken. Please choose another!');
            }
        }else{
            if(array[row][col] === false){
                array[row].splice(col, 1, 'O');
                player = 'X';
            }else{
                console.log('This place is already taken. Please choose another!');
            }
        }

        if(array[0][0] === array[0][1] && array[0][1] === array[0][2] && array[0][2] !== false) {
            console.log(`Player ${array[0][0]} wins!`);
            break;
        }
        if(array[1][0] === array[1][1] && array[1][1] === array[1][2] && array[1][2] !== false) {
            console.log(`Player ${array[1][0]} wins!`);
            break;
        }
        if(array[2][0] === array[2][1] && array[2][1] === array[2][2] && array[2][2] !== false) {
            console.log(`Player ${array[2][0]} wins!`);
            break;
        }
        if(array[0][0] === array[1][0] && array[1][0] === array[2][0] && array[2][0] !== false) {
            console.log(`Player ${array[0][0]} wins!`);
            break;
        }
        if(array[0][1] === array[1][1] && array[1][1] === array[2][1] && array[2][1] !== false) {
            console.log(`Player ${array[0][1]} wins!`);
            break;
        }
        if(array[0][2] === array[1][2] && array[1][2] === array[2][2] && array[2][2] !== false) {
            console.log(`Player ${array[0][2]} wins!`);
            break;
        }
        if(array[0][0] === array[1][1] && array[1][1] === array[2][2] && array[2][2] !== false) {
            console.log(`Player ${array[2][2]} wins!`);
            break;
        }
        if(array[0][2] === array[1][1] && array[1][1] === array[2][0] && array[2][0] !== false) {
            console.log(`Player ${array[2][0]} wins!`);
            break;
        }
        if(!array[0].includes(false) && !array[1].includes(false) && !array[2].includes(false)){
            console.log('The game ended! Nobody wins :(');
            break;
        }
    }   

    array.forEach(element => {
        console.log(element.join('\t'));
    });
}

ticTacToe(["0 1",
"0 0",
"0 2",
"2 0",
"1 0",
"1 2",
"1 1",
"2 1",
"2 2",
"0 0"]
);