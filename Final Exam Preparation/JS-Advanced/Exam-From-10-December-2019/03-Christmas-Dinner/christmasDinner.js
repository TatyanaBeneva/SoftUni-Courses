class ChristmasDinner{
    constructor(budget){
        this.budget = budget;
        this.dishes = [];
        this.products = [];
        this.guests = {};

        if(this.budget < 0){
            throw new Error("The budget cannot be a negative number");
        }
    }

    shopping([name, price]){
        if(this.budget < price){
            throw new Error("Not enough money to buy this product");
        } else{
            this.products.push(name);
            this.budget -= price;
            return `You have successfully bought ${name}!`;
        }
    }

    recipes(prepMeal){
        let isHave = true;
        prepMeal["productsList"].forEach(element =>{
            if(!this.products.includes(element)){
                isHave = false;
            }
        });

        if(isHave === false){
            throw new Error("We do not have this product");
        } else{
            this.dishes.push(prepMeal);
            return `${prepMeal["recipeName"]} has been successfully cooked!`;
        }
    }

    inviteGuests(name, dish){
        let isHave = false;
        for (const element of this.dishes) {
            if(element["recipeName"] === dish){
                isHave = true;
            }
        }

        if(isHave === false){
            throw new Error("We do not have this dish");
        }

        if(Object.keys(this.guests).includes(name)){
            throw new Error("This guest has already been invited");
        } else{
            this.guests[name] = dish;
            return `You have successfully invited ${name}!`
        }

    }

    showAttendance(){
        let result = [];
        Object.keys(this.guests).forEach(name =>{
            let allProducts = [];
            for (const dish of this.dishes) {
                if(dish["recipeName"] === this.guests[name]){
                    allProducts = dish["productsList"];
                }
            }
            result.push(`${name} will eat ${this.guests[name]}, which consists of ${allProducts.join(', ')}`);
        });
        return result.join('\n');
    }
}

let dinner = new ChristmasDinner(300);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);
dinner.recipes({
     recipeName: 'Oshav',
     productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});
dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});

dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');

console.log(dinner.showAttendance());
