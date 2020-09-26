class Library {
    _subscribers;
    _subscriptionTypes;

    constructor(libraryName){
        this.libraryName = libraryName;
        this._subscribers = [];
        this._subscriptionTypes = {
            normal: this.libraryName.length,
            special: this.libraryName.length * 2,
            vip: Number.MAX_SAFE_INTEGER
        }
    }

    subscribe(name, type){
        if(type !== 'normal' && type !== 'special' && type !== 'vip'){
            throw new Error(`The type ${type} is invalid`);
        }
        
        if(this._subscribers.map(x => x.name === name)){
            this._subscribers.push({name: name, type: type, books: []});
        } else{
            this._subscribers.map(x => {
                if(x.name === name){
                    x.type = type;
                }
            });
        }

        return this._subscribers.filter(x => x.name === name)[0];
    }

    unsubscribe(name){
        if(!this._subscribers.map(x => x.name === name)){
            throw new Error(`There is no such subscriber as ${name}`);            
        }
        let current = this._subscribers.filter(x => x.name === name);
        let index = this._subscribers.indexOf(current[0]);
        this._subscribers.splice(index,1);

        return this._subscribers;
    }

    receiveBook(subscriberName, bookTitle, bookAuthor){
        if(!this._subscribers.map(x => x.name === subscriberName)){
            throw new Error(`There is no such subscriber as ${subscriberName}`);            
        }

        this._subscribers.map(x => {
            if(x.name === subscriberName){
                for (const key in this._subscriptionTypes) {
                    if(key === x.type && this._subscriptionTypes[key] <= x.books.length){
                        throw new Error(`You have reached your subscription limit ${this._subscriptionTypes[key]}!`);
                    } else if(key === x.type && this._subscriptionTypes[key] > x.books.length){
                        x.books.push({title: bookTitle, author: bookAuthor});
                    }
                }
            }
        });

        return this._subscribers.filter(x => x.name === subscriberName)[0];
    }

    showInfo(){
        if(this._subscribers.length === 0){
            return `${this.libraryName} has no information about any subscribers`
        }

        let result = [];

        for (const sub of this._subscribers) {
            let booksArr = [];
            for (const book of sub.books) {
                booksArr.push(`${book.title} by ${book.author}`);
            }
            result.push(`Subscriber: ${sub.name}, Type: ${sub.type}`);
            result.push(`Received books: ${booksArr.join(', ')}`);
        }

        return result.join('\n');
    }
}

let lib = new Library('Lib');

lib.subscribe('Peter', 'normal');
lib.subscribe('John', 'normal');
lib.unsubscribe('Peter');
console.log(lib.receiveBook('John', 'A Song of Ice and Fire', 'George R. R. Martin'))
lib.receiveBook('John', 'Lord of the rings', 'J. R. R. Tolkien');


console.log(lib.showInfo());
