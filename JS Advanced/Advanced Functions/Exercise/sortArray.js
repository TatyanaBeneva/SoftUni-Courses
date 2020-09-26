function result(array, criteria){
    if(criteria === 'asc'){
        array.sort((a,b) => a - b);
    } else if( criteria === 'desc'){
        array.sort((a,b) => b - a);
    }

    let result = [];
    array.forEach(element => {
        result.push(element);
    });

    return result;
}

var inputArray = [3, 1, 2, 10];
var sortingMethod = 'asc';
var sortedArray = result(inputArray, sortingMethod);
console.log(sortedArray);