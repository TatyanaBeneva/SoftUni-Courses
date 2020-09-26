function addItem() {
    let inputText = document.getElementById('newItemText');
    let inputValue = document.getElementById('newItemValue');
    let selectMenu = document.getElementById('menu');
    let option = document.createElement('option');
    option.textContent = inputText.value;
    option.value = inputValue.value;
    selectMenu.appendChild(option);
    inputText.value = '';
    inputValue.value = '';
}