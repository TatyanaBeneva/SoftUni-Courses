function numbersSequense(n, k){
    const array = [1];
    
    for(let i = 1; i < n; i++){
        let sum = 0;
        
        for(let j = 1; j <= k; j++){
            if(array.length >= j){
                sum += Number(array[i - j]);
            }
        }

        array.push(sum);
    }

    console.log(array.join(' '));
}

numbersSequense(6,3);
numbersSequense(8,2);