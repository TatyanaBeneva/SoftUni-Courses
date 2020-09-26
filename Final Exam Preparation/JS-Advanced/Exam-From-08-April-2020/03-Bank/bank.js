class Bank {
    _bankName;
    constructor(_bankName){
        this._bankName = _bankName;
        this.allCustomers = [];
    }

    newCustomer(customer){
        for (const iterator of this.allCustomers) {
            if(iterator.personalId === customer.personalId){
                throw new Error(`${customer.firstName} ${customer.lastName} is already our customer!`);
            }
        }

        this.allCustomers.push(customer);
        return customer;
    }

    depositMoney(personalId, amount){
        if(!this.allCustomers.map(x => x.personalId === personalId)){
            throw new Error(`We have no customer with this ID!`);
        }

        this.allCustomers.map(x => {
            if(x.personalId === personalId){
                if(Object.keys(x).includes('transactions')){
                    x.totalMoney += Number(amount);
                    x.transactions.push({deposit: amount, id: x.transactions.length + 1});
                } else{   
                    x.totalMoney = amount;
                    x.transactions = [];                 
                    x.transactions.push({deposit: amount, id: x.transactions.length + 1});                    
                }
            }
        });

        let current = this.allCustomers.filter(x => x.personalId === personalId);
        return `${current[0].totalMoney}$`;
    }

    withdrawMoney (personalId, amount){
        if(!this.allCustomers.map(x => x.personalId === personalId)){
            throw new Error(`We have no customer with this ID!`);
        }

        this.allCustomers.map(x => {
            if(Object.keys(x).includes('totalMoney')){
                if(x.personalId === personalId && x.totalMoney >= amount){
                    x.totalMoney -= Number(amount);
                    x.transactions.push({withdraw: amount, id: x.transactions.length + 1});
                } else if(x.personalId === personalId && x.totalMoney < amount){
                    throw new Error(`${x.firstName} ${x.lastName} does not have enough money to withdraw that amount!`)
                }
            }
        })
        
        let current = this.allCustomers.filter(x => x.personalId === personalId);
        return `${current[0].totalMoney}$`;
    }

    customerInfo (personalId){
        if(!this.allCustomers.map(x => x.personalId === personalId)){
            throw new Error(`We have no customer with this ID!`);
        }
        let result = [];

        this.allCustomers.map(x => {
            if(x.personalId === personalId){
                result.push(`Bank name: ${this._bankName}`);
                result.push(`Customer name: ${x.firstName} ${x.lastName}`);
                result.push(`Customer ID: ${personalId}`);
                result.push(`Total Money: ${x.totalMoney}$`);
                result.push('Transactions:');
                x.transactions.sort((a, b) =>{
                    return b.id - a.id;
                })
                for (const tran of x.transactions) {
                    if(Object.keys(tran).includes('withdraw')){
                        result.push(`${tran.id}. ${x.firstName} ${x.lastName} withdrew ${tran.withdraw}$!`);
                    } else{
                        result.push(`${tran.id}. ${x.firstName} ${x.lastName} made deposit of ${tran.deposit}$!`)
                    }
                }
            }
        });

        return result.join('\n');
    }
}

let bank = new Bank('SoftUni Bank');


console.log(bank.newCustomer({firstName: 'Svetlin', lastName: 'Nakov', personalId: 6233267}));
// console.log(bank.newCustomer({firstName: 'Svetlin', lastName: 'Nakov', personalId: 6233267}));
console.log(bank.newCustomer({firstName: 'Mihaela', lastName: 'Mileva', personalId: 4151596}));

bank.depositMoney(6233267, 250);
console.log(bank.depositMoney(6233267, 250));
bank.depositMoney(4151596,555);

console.log(bank.withdrawMoney(6233267, 125));

console.log(bank.customerInfo(6233267));
