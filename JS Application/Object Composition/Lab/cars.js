function solve(input){
    let result = [];

    for(let i = 0; i < input.length; i++){
        let current = input[i].split(' ');

        if(current[0] === 'create'){

            result.push({name: current[1]});

            if(current.length > 2 && current[2] === 'inherit'){
                result.map(x => {
                    if(x.name === current[1]){

                        x.prototype = result.filter(c => c.name === current[3]);
                    }
                })
            }
        } else if(current[0] === 'set'){
            result.map(x => {
                if(x.name === current[1]){
                    x[current[2]] = current[3];
                }
            })
        } else if(current[0] === 'print'){
            let final = [];
            result.map(x => {
                if(x.name === current[1]){
                    for (const key in x) {
                        if(key !== 'name' && key !== 'prototype'){
                            final.push((`${key}:${x[key]}`));
                        } else if(key === 'prototype'){
                            for (const key2 in x[key]) {
                                if(key2 !== 'name'){
                                    final.push((`${key2}:${key[key2]}`));
                                }
                            }
                        }
                    }
                }
            })

            console.log(final.join(', '));
        }
    }
}

solve(['create c1',
'create c2 inherit c1',
'set c1 color red',
'set c2 model new',
'print c1',
'print c2']
);