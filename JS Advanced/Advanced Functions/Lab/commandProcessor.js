function solution(){
    var text ='';

    function append(str){
        text += str;
    }

    function removeStart(n){
        text = text.substring(n);
    }

    function removeEnd(n){
        text = text.substring(0, text.length - n);
    }

    function print(){
        console.log(text);
    }

    return {
        append,
        removeStart,
        removeEnd,
        print
    }
}

let firstZeroTest = solution();

firstZeroTest.append('hello');
firstZeroTest.append('again');
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);

firstZeroTest.print();

