function solve() {
    let taskInput = document.getElementById('task');
    let descriptionInput = document.getElementById('description');
    let dateInput = document.getElementById('date');
    let addButton = document.getElementById('add');
    let sections = document.getElementsByTagName('section');
    

    addButton.addEventListener('click', addButtonHandler);
    sections[1].addEventListener('click', startAndDeleteButtons);
    sections[2].addEventListener('click', deleteAndFinishButton);
    
    function deleteAndFinishButton(e){
        if(e.target.className === 'orange'){
            let divsOfComplate = sections[3].getElementsByTagName('div');
            let h3 = document.createElement('h3');
            h3.textContent = e.target.parentElement.previousSibling.previousSibling.previousSibling.innerText;
            let p1 = document.createElement('p');
            p1.textContent = e.target.parentElement.previousSibling.previousSibling.textContent;
            let p2 = document.createElement('p');
            p2.textContent = e.target.parentElement.previousSibling.textContent;
            let article = document.createElement('article');
            article.appendChild(h3);
            article.appendChild(p1);
            article.appendChild(p2);
            divsOfComplate[1].appendChild(article);     
            e.target.parentElement.parentElement.remove();
              
        } else if(e.target.className === 'red'){
            e.target.parentElement.parentElement.remove();
        }
    }

    function startAndDeleteButtons(e){
        if(e.target.className === 'green'){
            let divsOfPrgress = sections[2].getElementsByTagName('div');
            let h3 = document.createElement('h3');
            h3.textContent = e.target.parentElement.previousSibling.previousSibling.previousSibling.innerText;
            let p1 = document.createElement('p');
            p1.textContent = e.target.parentElement.previousSibling.previousSibling.textContent;
            let p2 = document.createElement('p');
            p2.textContent = e.target.parentElement.previousSibling.textContent;
            let div = document.createElement('div');
            div.className = "flex";
            let deleteButton = document.createElement('button');
            deleteButton.className = 'red';
            deleteButton.textContent = 'Delete';
            let finishButton = document.createElement('button');
            finishButton.className = 'orange';
            finishButton.textContent = 'Finish';
            let article = document.createElement('article');
            div.appendChild(deleteButton);
            div.appendChild(finishButton);
            article.appendChild(h3);
            article.appendChild(p1);
            article.appendChild(p2);
            article.appendChild(div);
            divsOfPrgress[1].appendChild(article);     
            e.target.parentElement.parentElement.remove();              
        } else if(e.target.className === 'red'){
            e.target.parentElement.parentElement.remove();
        }
    }

    function addButtonHandler(e){
        e.preventDefault();
        let validateInput = taskInput.value === '' 
                        || descriptionInput.value === '' 
                        || dateInput.value === '';

        if(!validateInput){
            let divs = sections[1].getElementsByTagName('div');
            let h3 = document.createElement('h3');
            h3.textContent = taskInput.value;
            let p1 = document.createElement('p');
            p1.textContent = `Description: ${descriptionInput.value}`;
            let p2 = document.createElement('p');
            p2.textContent = `Due Date: ${dateInput.value}`;
            let div = document.createElement('div');
            div.className = "flex";
            let startButton = document.createElement('button');
            startButton.className = 'green';
            startButton.textContent = 'Start';
            let deleteButton = document.createElement('button');
            deleteButton.className = 'red';
            deleteButton.textContent = 'Detele';
            let article = document.createElement('article');
            div.appendChild(startButton);
            div.appendChild(deleteButton);
            article.appendChild(h3);
            article.appendChild(p1);
            article.appendChild(p2);
            article.appendChild(div);
            divs[1].appendChild(article);
        }
    }
    
}