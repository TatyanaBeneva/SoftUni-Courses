function solve() {
    
    let button = document.querySelectorAll('exercise, button');
    let size = document.querySelectorAll('tbody tr').length;
    let validSudomu = true;

    button[0].addEventListener('click', (e) =>{
        let cells = Array.from(document.querySelectorAll('tbody input')).map(x => x.value);

        let parsedCells = [];

        for(let i = 0; i < size; i++){
            parsedCells.push([...cells.slice(i * size, (i + 1) * size)]);
        }

        for(let i = 0; i < size; i++){
            validSudomu = validSudomu ? (new Set(parsedCells[i])).size === size : false;
        }

        for(let col = 0; col < size; col++){
            let temp = [];

            for(let row = 0; row < size; row++){
                temp.push(parsedCells[row][col]);
            }

            validSudomu = validSudomu ? (new Set(temp)).size === size : false;

            
        }

        if(validSudomu === true){
            let tableBorder = document.getElementsByTagName('table')[0].style.border = '2px solid green';
            let paragraph = document.getElementsByTagName('p')[0];
            paragraph.textContent = 'You solve it! Congratulations!';
            paragraph.style.color = 'green';
        }else{
            let tableBorder = document.getElementsByTagName('table')[0].style.border = '2px solid red';
            let paragraph = document.getElementsByTagName('p')[0];
            paragraph.textContent = 'NOP! You are not done yet…';
            paragraph.style.color = 'red';
        }
        
        validSudomu = true;
    });

    button[1].addEventListener('click', (e) => {
        let cells = Array.from(document.querySelectorAll('tbody input')).map(x => x.value = '');
        let tableBorder = document.getElementsByTagName('table')[0].style.border = 'none';
        let paragraph = document.getElementsByTagName('p')[0].textContent = '';
    });
}