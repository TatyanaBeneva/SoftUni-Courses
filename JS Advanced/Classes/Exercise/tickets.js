function program(array, criteria){
    let infoData = [];
    array.forEach(element => {
        infoData.push(element.split('|'));
    });

    class Ticket {
        constructor(destination, price, status){
            this.destination = destination;
            this.price = Number(price);
            this.status = status;
        }
    }
    let result = [];

    infoData.forEach(x => {
        let info = new Ticket(x[0], x[1], x[2]);
        result.push(info);
    });
    result.sort((a, b) =>{
        let priceA = a.status;
        let priceB = b.status;
        if(criteria === 'destination'){
            priceA = a.destination;
            priceB = b.destination;
        } else if(criteria === 'price'){
            priceA = a.price;
            priceB = b.price;
        }

        if(priceA > priceB){
            return priceA - priceB;
        }

        return priceA.localeCompare(priceB);
    })
    return result;
}


console.log(program(['Philadelphia|94.20|available',
'New York City|95.99|available',
'New York City|95.99|sold',
'Boston|126.20|departed'],
'status'));
