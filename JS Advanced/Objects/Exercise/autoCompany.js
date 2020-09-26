function autoCompany(data){
    let parseData = data.reduce((acc, model) => {
        let [brand, carModel, producedCars] = model.split('|').map(x => x.trim());
        if(!acc[brand]){
            acc[brand] = {[carModel]: Number(producedCars)};
            return acc;
        }

        if(acc[brand][carModel]){
            acc[brand][carModel] += Number(producedCars);
        }else{
            acc[brand][carModel] = Number(producedCars);
        }

        return acc;
    }, {});
    
    for (const key in parseData) {
        console.log(key);

        for (const nextKey in parseData[key]) {
            console.log(`###${nextKey} -> ${parseData[key][nextKey]}`);
        }
    }
}

autoCompany(['Audi | Q7 | 1000',
'Audi | Q6 | 100',
'BMW | X5 | 1000',
'BMW | X6 | 100',
'Citroen | C4 | 123',
'Volga | GAZ-24 | 1000000',
'Lada | Niva | 1000000',
'Lada | Jigula | 1000000',
'Citroen | C4 | 22',
'Citroen | C5 | 10']
);