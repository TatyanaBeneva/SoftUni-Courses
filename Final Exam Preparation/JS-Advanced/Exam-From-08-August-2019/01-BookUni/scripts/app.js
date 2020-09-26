function solve() {
    let inputs = document.querySelectorAll('form input');
    let button = document.querySelector('form button');
    let divs = document.querySelectorAll('#outputs .bookShelf');
    let totalProfit = document.getElementsByTagName('h1')[1];
    let divNewAndOld = document.getElementById('outputs');
    let totalPrice = 0;

    button.addEventListener('click', addNewBook);
    divNewAndOld.addEventListener('click', newAndOldHandler);

    function newAndOldHandler(e){
        if(e.target.parentElement.parentElement.previousElementSibling.textContent === 'Old Books'){
            let price = (Number(inputs[2].value) * 0.85).toFixed(2);
            totalPrice += Number(price);
            totalProfit.textContent = `Total Store Profit: ${totalPrice.toFixed(2)} BGN`;
            e.target.parentElement.remove();
        } else if(e.target.parentElement.parentElement.previousElementSibling.textContent === 'New Books'){
            if(e.target.textContent.includes('Buy')){
                let price = Number(inputs[2].value).toFixed(2);
                totalPrice += Number(price);
                totalProfit.textContent = `Total Store Profit: ${totalPrice.toFixed(2)} BGN`;
                e.target.parentElement.remove();
            } else if(e.target.textContent.includes('Move')){
                let price = Number(inputs[2].value).toFixed(2);
                let paragraph = e.target.previousElementSibling.previousElementSibling;
                let buyButton = e.target.previousElementSibling;
                buyButton.textContent = `Buy it only for ${(price * 0.85).toFixed(2)} BGN`;
                let bookDiv = document.createElement('div');
                bookDiv.appendChild(paragraph);
                bookDiv.appendChild(buyButton);
                bookDiv.className = 'book';
                divs[0].appendChild(bookDiv);
                e.target.parentElement.remove();
            }
        }
    }

    function addNewBook(e){
        e.preventDefault();
        let nameOfBook = inputs[0].value;
        let year = inputs[1].value;
        let price = Number(inputs[2].value).toFixed(2);
        let bookDiv = document.createElement('div');
        bookDiv.className = 'book';
        let paragraph = document.createElement('p');
        paragraph.textContent = `${nameOfBook} [${year}]`;
        let buyButton = document.createElement('button');
        buyButton.textContent = `Buy it only for ${price} BGN`;

        if(year >= 2000){
            buyButton.textContent = `Buy it only for ${price} BGN`;
            let oldButton = document.createElement('button');
            oldButton.textContent = "Move to old section";
            bookDiv.appendChild(paragraph);
            bookDiv.appendChild(buyButton);
            bookDiv.appendChild(oldButton);
            if(nameOfBook.length > 0 && year > 0 && price > 0)
            divs[1].appendChild(bookDiv);
        } else{
            buyButton.textContent = `Buy it only for ${(price * 0.85).toFixed(2)} BGN`
            bookDiv.appendChild(paragraph);
            bookDiv.appendChild(buyButton);
            if(nameOfBook.length > 0 && year > 0 && price > 0)
            divs[0].appendChild(bookDiv);
        }        
    }
}