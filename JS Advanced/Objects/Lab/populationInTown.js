function populationInTown(input){
    let result = {};
    for(let i = 0; i < input.length; i++){
        const info = input[i].split(' <-> ');
        let [town, population] = [info[0], Number(info[1])];
        if (result[town] == undefined) {
            result[town] = population;
        } else {
            result[town] += population;
        }
    }

    for (const key in result) {
        console.log(`${key} : ${result[key]}`);
    }
}

populationInTown(['Istanbul <-> 100000',
'Honk Kong <-> 2100004',
'Jerusalem <-> 2352344',
'Mexico City <-> 23401925',
'Istanbul <-> 1000']
);