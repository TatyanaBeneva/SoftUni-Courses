function solve(array){
    let result = [];

    for(let i = 0; i < array.length; i++){
        let currentComand = array[i];
        
        if(currentComand === 'print'){
            function closure(){
                console.log(result.join(','));
            }
        } else{
            let current = currentComand.split(' ');

            if(current[0] === 'add'){
                result.push(current[1]);
            } else{
                let index = result.indexOf(current[1], 0);
                result.splice(index, 1);
            }
        }        
    }

    return closure();
}

solve(['add pesho', 'add george', 'add peter', 'remove peter','print']);