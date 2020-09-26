function result(value){
    value = interceptor(value);
    value = function(value){
        value = Number(value);
        let current = Math.trunc(value) + ',';
        current += value.toFixed(2).substr(-2,2);
        return '$ ' + current;
    }

    return value;
}

function interceptor(separator, symbol, symbolFirst, value) {
    return [separator, symbol, symbolFirst, value];
}
let intercepted = result(interceptor);


let [separator, symbol, symbolFirst, value] = intercepted(1);
