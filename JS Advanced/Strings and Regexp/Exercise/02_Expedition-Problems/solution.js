function solve() {
    let key = document.getElementById('string').value;
    let message = document.getElementById('text').value;
    let result = document.getElementById('result');
    let saveMessage = message.match(`${key}(.+)${key}`)[1];
    let ourRegex = new RegExp(/(east|north).*?(\d{2}).*?,.*?(\d{6})/gmi);
    let north;
    let east;
    let temp = ourRegex.exec(message);
    while(temp){
        if(temp[1].toLowerCase() === 'east'){
            east = `${temp[2]}.${temp[3]}`;
        }else{
            north = `${temp[2]}.${temp[3]}`;
        }

        temp = ourRegex.exec(message);
    };

    result.innerHTML = `
    <p>${north} N</p>
    <p>${east} E</p>
    <p>Message : ${saveMessage}</p>
    `;
}