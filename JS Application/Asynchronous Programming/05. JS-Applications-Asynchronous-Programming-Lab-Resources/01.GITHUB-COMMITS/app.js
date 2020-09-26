async function loadCommits() {
    // Try it with Fetch API
    let username = document.getElementById('username').value;
    let repo = document.getElementById('repo').value;
    let container = document.getElementById('commits');
    container.innerText = '';

    try {
        let response = await fetch(`https://api.github.com/repos/${username}/${repo}/commits`);

        if(response.status < 400){
            let data = await response.json();
            data.forEach(element => {
                let li = document.createElement('li');
                li.innerText = `${element.commit.author.name}: ${element.commit.message}`;
                container.appendChild(li);
            })
        } else{
            throw({
                status: response.status,
                statusText: response.statusText
            });
        }

    } catch (err) {
        let li = document.createElement('li');
        li.innerText = `Error: ${err.status} (${err.statusText})`;
        container.appendChild(li);
    }

    // fetch(`https://api.github.com/repos/${username}/${repo}/commits`)
    //     .then((response) => {
    //         if(response.status < 400){
    //             return response.json();
    //         }

    //         throw({
    //             status: response.status,
    //             statusText: response.statusText
    //         });
    //     })
    //     .then((data) => {
    //         data.forEach(element => {
    //             let li = document.createElement('li');
    //             li.innerText = `${element.commit.author.name}: ${element.commit.message}`;
    //             container.appendChild(li);
    //         })
    //     })
    //     .catch((err) => {
    //         let li = document.createElement('li');
    //         li.innerText = `Error: ${err.status} (${err.statusText})`;
    //         container.appendChild(li);
    //     });
}