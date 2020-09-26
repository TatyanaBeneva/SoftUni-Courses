function test(){
    let sum = 0;
    function add(addend){
        sum += addend;

        return add;
    };

    add.toString = function(){
        return sum;
    }

    return add;
}

let add = test();


console.log(add(1)(6)(-3).toString());