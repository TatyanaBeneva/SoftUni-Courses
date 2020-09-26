function lowestPriceInCities(input){
    const finalArray = [];

    for (const iterator of input) {
        const array = iterator.split(' | ');
        finalArray.push(array);
    }
    const result = [];

    for (const array of finalArray) {
        let minPrice = Number(array[2]);
        let product = array[1];
        let town = array[0];
        if(!result.includes(array[1])){
            for (const iterator of finalArray) {
                if(array[1] === iterator[1]){
                    if(minPrice > Number(iterator[2])){
                        minPrice = Number(iterator[2]);
                        product = iterator[1];
                        town = iterator[0];
                    }
                }
            }

            result.push(town, product, minPrice);
        }
    }

    for(let i = 0; i < result.length; i += 3){
        console.log(`${result[i + 1]} -> ${result[i + 2]} (${result[i]})`);
    } 
}

lowestPriceInCities(['Sofia City | Audi | 100000',
    'Sofia City | BMW | 100000',
    'Sofia City | Mitsubishi | 10000',
    'Sofia City | Mercedes | 10000',
    'Sofia City | NoOffenseToCarLovers | 0',
    'Mexico City | Audi | 1000',
    'Mexico City | BMW | 99999',
    'New York City | Mitsubishi | 10000',
    'New York City | Mitsubishi | 1000',
    'Mexico City | Audi | 100000',
    'Washington City | Mercedes | 1000']
);