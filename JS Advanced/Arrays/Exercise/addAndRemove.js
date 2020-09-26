function addAndRemove(input){
    const result = [];
    let count = 0;
    for(let i = 0; i < input.length; i++){
        count++;
        if(input[i] === 'add'){
            result.push(count);
        }else if(input[i] === 'remove'){
            result.pop();
        }
    }

    if(result.length > 0){
        result.forEach(item => {
            console.log(item);
        });
    }else{
        console.log('Empty');
    }
}

addAndRemove(['add', 
'add', 
'remove', 
'add', 
'add']
);