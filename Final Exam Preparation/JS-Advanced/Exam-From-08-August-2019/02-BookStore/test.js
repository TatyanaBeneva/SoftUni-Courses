let BookStore = require('./02. Book Store_Ресурси');
let assert = require('chai').assert;

describe('BookStore class beahvior', ()=>{
    let bs;

    beforeEach(function(){
        bs = new BookStore('Helikon');
    });

    describe('constructor', ()=>{
        it('name string parameter of constructor', ()=>{
            assert.deepEqual(bs, new BookStore('Helikon'));
        });

        it('books param', ()=>{
            assert.deepEqual(bs.books, []);
        });

        it('workers param', ()=>{
            assert.deepEqual(bs._workers, []);
        });
    });

    describe('stockBooks method', ()=>{
        it('return object of books', ()=>{
            assert.deepEqual(bs.stockBooks(['Devil-Hill']), bs.books = [{'title': 'Devil', 'author': 'Hill'}]);
        });
    });

    describe('hire method', ()=>{
        it('throw error if worker is already hired', ()=>{
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 1}];
            assert.throw(()=> bs.hire('Sara', 'cleaner'), 'This person is our employee');
        });

        it('add worker to the workers array', ()=>{
            assert.deepEqual(bs.hire('Sara', 'casher'), `Sara started work at Helikon as casher`);
        });

        it('add worker to the workers array', ()=>{
            bs.hire('Sara', 'casher')
            assert.deepEqual(bs._workers, [{'name': 'Sara', 'position': 'casher', 'booksSold': 0}]);
        });
    });

    describe('fire method', ()=>{
        it('remove worker if the name exist in workers', ()=>{
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 1}];
            assert.deepEqual(bs.fire('Sara'), `Sara is fired`);
        });

        it('remove worker if the name exist in workers', ()=>{
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 1}];
            bs.fire('Sara');
            assert.deepEqual(bs._workers, []);
        });

        it('throw error if the name do not exist in workers', ()=>{
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 1}];
            assert.throw(()=> bs.fire('Meri'), `Meri doesn't work here`);
        });
    });

    describe('sellBook method', ()=>{
        it('throw error if book is not in stock', ()=>{
            bs.books = [{'title': 'Devil', 'author': 'Hill'}]
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 0}];
            assert.throw(()=> bs.sellBook('Angel', 'Sara'), 'This book is out of stock');
        });

        it('throw error if worker is not exist', ()=>{
            bs.books = [{'title': 'Devil', 'author': 'Hill'}]
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 0}];
            assert.throw(()=> bs.sellBook('Devil', 'Meri'), `Meri is not working here`);
        });

        it('if we have existing title and worker', ()=>{
            bs.books = [{'title': 'Devil', 'author': 'Hill'}];
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 0}];
            bs.sellBook('Devil', 'Sara');
            assert.deepEqual(bs._workers, [{'name': 'Sara', 'position': 'casher', 'booksSold': 1}]);
        });
    });

    describe('printWorkers method', ()=>{
        it('print all names', ()=>{
            bs._workers = [{'name': 'Sara', 'position': 'casher', 'booksSold': 2}];
            assert.deepEqual(bs.printWorkers(), 
            `Name:Sara Position:casher BooksSold:2`);
        });
    });
});