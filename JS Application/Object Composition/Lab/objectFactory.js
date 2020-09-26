function solve(input){
    var array = JSON.parse(input);
    let result = array[0];
    for(let i = 1; i < array.length; i++){
        result = Object.assign(result, array[i]);
    }

    console.log(result);
}

solve(`[{"canFly": true},{"canMove":true, "doors": 4},{"capacity": 255},{"canFly":true, "canLand": true}]`);