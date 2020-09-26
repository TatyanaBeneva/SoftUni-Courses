function solution() {
    let sections = document.getElementsByTagName('section');
    let addGiftsButton = sections[0].querySelector('button');
    let listOfGifts = sections[1].querySelector('ul');
    let listOfSendGifts = sections[2].querySelector('ul');
    let listOfDiscardGifts = sections[3].querySelector('ul');
    let sortedList = [];
    
    addGiftsButton.addEventListener('click', addGiftsButtonHandler);
    listOfGifts.addEventListener('click', sendAndDiscardButtonHandler);

    function sendAndDiscardButtonHandler(e){
        if(e.target.id === 'sendButton'){
            let nameOfGift = e.target.parentElement.textContent.replace('Send', '').replace('Discard', '');
            let listElementOfGifts = e.target.parentElement;
            let listOfSends = document.createElement('li');
            listOfSends.className = 'gift';
            listOfSends.textContent = nameOfGift;
            listOfSendGifts.appendChild(listOfSends);
            listOfGifts.removeChild(listElementOfGifts);
            let index = sortedList.indexOf(listElementOfGifts);
            sortedList.splice(index, 1);
        }else if(e.target.id === 'discardButton'){
            let nameOfGift = e.target.parentElement.textContent.replace('Send', '').replace('Discard', '');
            let listElementOfGifts = e.target.parentElement;
            let listOfSends = document.createElement('li');
            listOfSends.className = 'gift';
            listOfSends.textContent = nameOfGift;
            listOfDiscardGifts.appendChild(listOfSends)
            listOfGifts.removeChild(listElementOfGifts);
            let index = sortedList.indexOf(listElementOfGifts);
            sortedList.splice(index, 1);
        }
    }

    function addGiftsButtonHandler(){
        let giftName = sections[0].querySelector('input');
        let listElement = document.createElement('li');
        listElement.className = 'gift';
        listElement.textContent = giftName.value;
        let sendButton = document.createElement('button');
        sendButton.setAttribute("id", 'sendButton');
        sendButton.textContent = 'Send';
        listElement.appendChild(sendButton);
        let discardButton = document.createElement('button');
        discardButton.setAttribute("id", 'discardButton');
        discardButton.textContent = 'Discard';
        listElement.appendChild(discardButton);
        sortedList.push(listElement);
        sortedList = sortedList.sort((a,b) => a - b);
        for(let i = 0; i < sortedList.length; i++){
            listOfGifts.appendChild(sortedList[i]);
        }
        giftName.value = '';
    }
}