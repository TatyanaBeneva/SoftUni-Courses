function rotateArray(input){
    let rotationCount = Number(input.pop());
    if(rotationCount > input.length){
        rotationCount %= input.length;
    }

    for(let i = 0; i < rotationCount; i++){
        let lastElement = input.pop();
        input.splice(0,0,lastElement);
    }

    console.log(input.join(' '));
}

rotateArray(['Banana', 
'Orange', 
'Coconut', 
'Apple', 
'15']
);