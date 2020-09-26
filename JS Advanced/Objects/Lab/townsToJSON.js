function townsToJson(input){
    const obj = [];
    for(let i = 0; i < input.length - 1; i++){        
        const infoTown = input[i + 1].split(/\s*\|\s*/);
        let townName = infoTown[1];
        let latitudeScore = Number(infoTown[2]).toFixed(2);
        let longitudeScore = Number(infoTown[3]).toFixed(2);
        obj.push({ "Town": townName,
         "Latitude": Number(latitudeScore), 
         "Longitude": Number(longitudeScore) });
    } 

    let myJson = JSON.stringify(obj);
    console.log(myJson);
}

townsToJson(['| Town | Latitude | Longitude |',
'| Sofia | 42.696552 | 23.32601 |',
'| Beijing | 39.913818 | 116.363625 |']
);