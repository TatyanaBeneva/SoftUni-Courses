(() => {
    //getting all the elements from the html document that we need to use
    const elements = {
        anglerInputAdd: document.querySelector('#addForm input.angler'),
        weightInputAdd: document.querySelector('#addForm input.weight'),
        speciesInputAdd: document.querySelector('#addForm input.species'),
        locationInputAdd: document.querySelector('#addForm input.location'),
        baitInputAdd: document.querySelector('#addForm input.bait'),
        captureTimeInputAdd: document.querySelector('#addForm input.captureTime'),
        addBtn: document.querySelector('#addForm button.add'),
        loadBtn: document.querySelector('.load'),
        updateBtn: document.querySelector('.update'),
        deleteBtn: document.querySelector('.delete'),
        anglerInput: document.querySelector('.catch input.angler'),
        weightInput: document.querySelector('.catch input.weight'),
        speciesInput: document.querySelector('.catch input.species'),
        locationInput: document.querySelector('.catch input.location'),
        baitInput: document.querySelector('.catch input.bait'),
        captureTimeInput: document.querySelector('.catch input.captureTime'),
        divCatch: document.querySelector('.catch'),
        mainDiv: document.querySelector('#catches')
    };

    const CREATE_URL = "https://fisher-game.firebaseio.com/catches.json";
    const DELETE_UTL = "https://fisher-game.firebaseio.com/catches/{catchId}.json";
    elements.addBtn.addEventListener('click', addCatch);
    elements.loadBtn.addEventListener('click', getAllCatches);
    elements.mainDiv.addEventListener('click', (e) => {
        if(e.target.textContent === 'Delete'){
            deleteCatch(e.target);
        } else if(e.target.textContent === 'Update'){
            updateCatch(e.target);
        }
    });

    async function addCatch(){
        let myCatch = {
            angler: elements.anglerInputAdd.value,
            weight: elements.weightInputAdd.value,
            species: elements.speciesInputAdd.value,
            location: elements.locationInputAdd.value,
            bait: elements.baitInputAdd.value,
            captureTime: elements.captureTimeInputAdd.value
        };

        const options = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(myCatch)
        };

        try {
            const response = await fetch(CREATE_URL, options);
            const data = await response.json();  

            elements.anglerInputAdd.value = '';
            elements.weightInputAdd.value = '';
            elements.speciesInputAdd.value = '';
            elements.baitInputAdd.value = '';
            elements.locationInputAdd.value = '';
            elements.captureTimeInputAdd.value = '';

        } catch (error) {
            console.error(error);
        }
    }

    async function updateCatch(e){
        let divCatch = e.parentElement;
        let catchId = divCatch.getAttribute('data-id');
        const url = DELETE_UTL.replace('{catchId}', catchId);

        let myCatch = {
            angler: divCatch.querySelector('.angler').value,
            weight: divCatch.querySelector('.weight').value,
            species: divCatch.querySelector('.species').value,
            location: divCatch.querySelector('.location').value,
            bait: divCatch.querySelector('.bait').value,
            captureTime: divCatch.querySelector('.captureTime').value
        }

        const options = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(myCatch)
        };

        try {
            let response = await fetch(url, options);
            let data = await response.json();
        } catch (error) {
            console.error(error);
        }
    }

    async function deleteCatch(e){
        let parent = e.parentElement;
        let catchId = parent.getAttribute('data-id');
        const url = DELETE_UTL.replace('{catchId}', catchId);

        const options = {
            method: 'DELETE',
            headers: {'Content-Type': 'application/json'}
        };

        try {
            let response = await fetch(url, options);
            let data = await response.json();
        } catch (error) {
            console.error(error);
        }

        elements.mainDiv.removeChild(parent);

    }

    async function getAllCatches(){

        try {
            let response = await fetch(CREATE_URL);
            let data = await response.json();
            loadCathes(data);
        } catch (error) {
            console.error(error);
        }
    }

    function loadCathes(data){
        elements.mainDiv.innerHTML = '';

        Object.keys(data).forEach(id => {
            let divCatch = createHTMLElement('div', ['catch']);
            divCatch.setAttribute('data-id', id);
            let lableA = createHTMLElement('lable',[], 'Angler');
            let lableW = createHTMLElement('lable',[], 'Weight');
            let lableS = createHTMLElement('lable',[], 'Species');
            let lableL = createHTMLElement('lable',[], 'Location');
            let lableB = createHTMLElement('lable',[], 'Bait');
            let lableC = createHTMLElement('lable',[], 'Capture Time');
            let inputA = createHTMLElement('input',['angler']);
            inputA.setAttribute('type', "text");
            inputA.value = data[id].angler;
            let inputW = createHTMLElement('input',['weight']);
            inputW.setAttribute('type', "number");
            inputW.value = data[id].weight;
            let inputS = createHTMLElement('input',['species']);
            inputS.setAttribute('type', "text");
            inputS.value = data[id].species;
            let inputL = createHTMLElement('input',['location']);
            inputL.setAttribute('type', "text");
            inputL.value = data[id].location;
            let inputB = createHTMLElement('input',['bait']);
            inputB.setAttribute('type', "text");
            inputB.value = data[id].bait;
            let inputC = createHTMLElement('input',['captureTime']);
            inputC.setAttribute('type', "number");
            inputC.value = data[id].captureTime;
            let updateBtn = createHTMLElement('button', ['update'], 'Update');
            let deleteBtn = createHTMLElement('button', ['delete'], 'Delete');
            let hr = createHTMLElement('hr');
            divCatch.appendChild(lableA);
            divCatch.appendChild(inputA);
            divCatch.appendChild(hr);
            divCatch.appendChild(lableW);
            divCatch.appendChild(inputW);
            divCatch.appendChild(hr);
            divCatch.appendChild(lableS);
            divCatch.appendChild(inputS);
            divCatch.appendChild(hr);
            divCatch.appendChild(lableL);
            divCatch.appendChild(inputL);
            divCatch.appendChild(hr);
            divCatch.appendChild(lableB);
            divCatch.appendChild(inputB);
            divCatch.appendChild(hr);
            divCatch.appendChild(lableC);
            divCatch.appendChild(inputC);
            divCatch.appendChild(hr);
            divCatch.appendChild(updateBtn);
            divCatch.appendChild(deleteBtn);
            elements.mainDiv.appendChild(divCatch);
        })
    }

    function createHTMLElement(tagName, className, textContent){
        let element = document.createElement(tagName);

        if(className){
            element.classList.add(...className);
        }

        if(textContent){
            element.textContent = textContent;
        }

        return element;
    }
})();
