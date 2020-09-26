function arrayMap(nums, func){
    let result = [];
    nums.reduce(function(acc, cur){
        result.push(func(cur));
        return acc;
    },0);

    return result;
}

let letters = ["a","b","c"];
console.log(arrayMap(letters,(l)=>l.toLocaleUpperCase())) // [ 'A', 'B', 'C' ]

