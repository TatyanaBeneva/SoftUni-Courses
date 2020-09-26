function subtract() {
    let input1 = document.getElementById('firstNumber');
    let input2 = document.getElementById('secondNumber');
    let resultDiv = document.getElementById('result');
    let sum = Number(input1.value) - (Number(input2.value));
    resultDiv.textContent = sum;
}