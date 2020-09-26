function solve(area, vol, input) {
    let result = [];
    
    for(let i = 0; i < input.length; i++){
        this.x = input[i].x;
        this.y = input[i].y;
        this.z = input[i].z;
        result.push({area: Math.abs(area()), volume: Math.abs(vol())});
    }
    return result;
}

function area() {
    return this.x * this.y;
};

function vol() {
    return this.x * this.y * this.z;
};

console.log(solve(area, vol, [
    {"x":"10","y":"-22","z":"10"},
    {"x":"47","y":"7","z":"-5"},
    {"x":"55","y":"8","z":"0"},
    {"x":"100","y":"100","z":"100"},
    {"x":"55","y":"80","z":"250"}
    ]   
    ));
