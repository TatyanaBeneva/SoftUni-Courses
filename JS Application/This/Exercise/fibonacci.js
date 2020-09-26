function getFibonator(){
    let prevFib = 0;
    let curFib = 1;

    return function(){
        let result = curFib;
        [curFib, prevFib] = [prevFib + curFib, curFib];
        return result;
    }
}
let fib = getFibonator();
console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());
