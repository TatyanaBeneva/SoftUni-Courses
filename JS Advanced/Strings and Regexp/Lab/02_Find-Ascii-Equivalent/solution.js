function solve() {
  let input = document.getElementById('text').value;
  let result = document.getElementById('result');
  let numbers = input.match(/\d+/g);
  let words = input.match(/[A-Za-z]+|[^\d\sA-Za-z]/g);
  let output = '';
  
  for (const char of words) {
    let charToNum = [];
    for(let i = 0; i < char.length; i++){
      charToNum.push(char[i].charCodeAt(0));
    }
    result.innerHTML += `<br/>${charToNum.join(' ')}`;
  }

  for (const num of numbers) {
    output += String.fromCharCode(num);
  }
  
  result.innerHTML += `<br/>${output}`;
}