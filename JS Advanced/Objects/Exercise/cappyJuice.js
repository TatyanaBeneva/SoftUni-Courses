function juiceFactory(data){
    let parseData = {};
    let juice = {};
    for(let i = 0; i < data.length; i++){
        let tempParsedJuice = data[i].split(' => ');
        if(parseData[tempParsedJuice[0]] != undefined){
            parseData[tempParsedJuice[0]] += Number(tempParsedJuice[1]);
        }else{
            parseData[tempParsedJuice[0]] = Number(tempParsedJuice[1]);
        }

        let bottleQ = Math.floor(parseData[tempParsedJuice[0]] / 1000);
        if(bottleQ > 0){
            juice[tempParsedJuice[0]] = bottleQ;
        }
    }

    let finaleParseData = Object.entries(juice);
    for(let i = 0; i < finaleParseData.length; i++) {
        console.log(finaleParseData[i].join(' => '));   
    }
}

juiceFactory(['Kiwi => 234',
'Pear => 2345',
'Watermelon => 3456',
'Kiwi => 4567',
'Pear => 5678',
'Watermelon => 6789']
);