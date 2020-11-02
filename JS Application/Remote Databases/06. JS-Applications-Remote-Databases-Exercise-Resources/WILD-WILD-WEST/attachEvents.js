function attachEvents() {
    const apiKey = ""; // firebase url
    let playerNameInput = document.getElementById('addName');
    let addPlayerButton = document.getElementById('addPlayer');
    let playersList = document.getElementById('players');
    let saveButton = document.getElementById('save');
    let reloadButton = document.getElementById('reload');
    let canvas = document.getElementById('canvas');

    function playerTemplate(output, key){
        return `
        <div class="player" data-id=${key}>
        <div class="row">
            <label>Name:</label>
            <label class="name">${output[key].name}</label>
        </div>
        <div class="row">
            <label>Money:</label>
            <label class="money">${output[key].money}</label>
        </div>
        <div class="row">
            <label>Bullets:</label>
            <label class="bullets">${output[key].bullets}</label>
        </div>
        <button class="play">Play</button>
        <button class="delete">Delete</button>
        </div>
      `;
    }

    playersList.addEventListener('click', (e) => {
        if(e.target.textContent === 'Play'){
            let divPlayer = e.target.parentElement;
            let id = divPlayer.getAttribute('data-id');
            saveButton.style.display = 'block';
            reloadButton.style.display = 'block';
            canvas.style.display = 'block';
            let currentPlayer = {};
            let bullets = divPlayer.getElementsByClassName('bullets')[0];
            let money = divPlayer.getElementsByClassName('money')[0];

            fetch(apiKey + 'players.json')
            .then(x => x.json())
            .then(x => {
                for (const key in x) {
                    if(key === id){
                        currentPlayer.name = x[key].name;
                        currentPlayer.money = x[key].money;
                        currentPlayer.bullets = x[key].bullets;
                    }
                }
            });

            loadCanvas(currentPlayer)

            saveButton.addEventListener('click', e => {
                saveButton.style.display = 'none';
                reloadButton.style.display = 'none';
                canvas.style.display = 'none';
                
                fetch(`${apiKey}players/${id}.json`, {
                    method: "PUT",
                    body: JSON.stringify(currentPlayer)
                })
                .then(x => x.json());

                clearInterval(canvas.intervalId);
                bullets.textContent = currentPlayer.bullets;
                money.textContent = currentPlayer.money;                
            })

            reloadButton.addEventListener('click', e =>{
                currentPlayer.money -= 60;
                currentPlayer.bullets = 6;
            })
        }
    })

    addPlayerButton.addEventListener('click', (e)=>{
        const bodyPlayer = {
            'name': playerNameInput.value,
            'money': 500,
            'bullets': 6
        };
    
        fetch(apiKey + "players.json", {
            method: "POST",
            body: JSON.stringify(bodyPlayer)
        })
        .then(x => x.json());
    
        playerNameInput.value = '';
    });

    fetch(apiKey + 'players.json')
    .then(x => x.json())
    .then(x => {
        for (const key in x) {
          playersList.innerHTML += playerTemplate(x, key);
        }
    });
}