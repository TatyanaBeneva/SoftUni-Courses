function systemComponent(data){
    let parseData = data.reduce((db, componentData) => {
        let [systemName, componentName, subComponentName] = componentData.split('|').map(x => x.trim());
        if(!db[systemName]){
            db[systemName] = {[componentName]: [subComponentName]};
            return db;
        }

        if(!db[systemName][componentName]){
            db[systemName][componentName] = [subComponentName];
        }

        if(!db[systemName][componentName].includes(subComponentName)){
            db[systemName][componentName] = [...db[systemName][componentName], subComponentName];
        }

        return db;
    }, {});

    console.log(parseData);

    let sortedSystems = Object.keys(parseData).sort((a,b) => {
        if(Object.keys(parseData[a]).length === Object.keys(parseData[b]).length){
            if(a > b) return 1
            if(a < b) return -1
        }else{
            return Object.keys(parseData[a]).length < Object.keys(parseData[b]).length;
        }        
    });

    sortedSystems.forEach(element => {
        console.log(element);
        let system = parseData[element];
        let componentSortedKeys = Object.keys(system).sort((a,b) => {
            return system[a].length < system[b]. length;
        });

        componentSortedKeys.forEach(component => {
            console.log(`|||${component}`);
            system[component].forEach(subcomponent => {
                console.log(`||||||${subcomponent}`);
            });
        });
    });
}

systemComponent(['SULS | Main Site | Home Page',
'SULS | Main Site | Login Page',
'SULS | Main Site | Register Page',
'SULS | Judge Site | Login Page',
'SULS | Judge Site | Submittion Page',
'Lambda | CoreA | A23',
'SULS | Digital Site | Login Page',
'Lambda | CoreB | B24',
'Lambda | CoreA | A24',
'Lambda | CoreA | A25',
'Lambda | CoreC | C4',
'Indice | Session | Default Storage',
'Indice | Session | Default Security']
);