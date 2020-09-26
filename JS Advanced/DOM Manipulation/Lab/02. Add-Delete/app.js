function addItem() {
    
    let input = document.getElementById('newText');
    let list = document.getElementById('items');
    let child = document.createElement('li'); 
    let link = document.createElement('a');
    link.href = '#';
    link.textContent ='[Delete]';
    

    if(input.value.length > 0){
        child.textContent = input.value + ' ';
        list.appendChild(child);
        child.appendChild(link);
        input.value = '';        
    }

    link.addEventListener('click', (e) =>{
        list.removeChild(child);
    })
}
