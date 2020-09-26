function addItem() {
    let input = document.getElementById('newItemText');
    let list = document.getElementById('items');
    let child = document.createElement('li');   

    if(input.value.length > 0){
        child.textContent = input.value;
        list.appendChild(child);
        input.value = '';
    }
}