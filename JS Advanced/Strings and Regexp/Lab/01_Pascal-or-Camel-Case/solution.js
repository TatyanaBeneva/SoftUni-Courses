function solve() {
    let input = document.getElementById('text').value;
    let convention = document.getElementById('naming-convention').value;
    let finalResult = document.getElementById('result');
    let arrayOfInput = input.toLowerCase().split(' ').filter(a => a !== '');
    let result = '';
    
    if(convention === 'Camel Case'){
      for (let word of arrayOfInput) {
        let output = word;
        result += output.replace(output[0], output[0].toUpperCase());
      }
      result = result.replace(result[0], result[0].toLowerCase());
    } else if(convention === 'Pascal Case'){
      for (let word of arrayOfInput) {
        let output = word;
        result += output.replace(output[0], output[0].toUpperCase());
      }
    } else{
      result = 'Error!';
    }

    finalResult.textContent = result;
    result = '';
}