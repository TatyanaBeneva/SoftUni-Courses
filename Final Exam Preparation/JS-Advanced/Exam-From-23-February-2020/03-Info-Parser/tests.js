let Parser = require("./solution.js");
let assert = require("chai").assert;

describe("MyTests", () => {
    let pr;

    beforeEach(function(){
        pr = new Parser('[ {"Nancy":"architect"} ]');
    });

    describe('constructor of the class', ()=>{
        it('data to be parsed', ()=>{
            assert.deepEqual(pr._data, [ { Nancy: 'architect' } ]);
        });

        it('log to be []', ()=>{
            assert.deepEqual(pr._log, []);
        });

        it('addToLog to be function', ()=>{
            assert.isFunction(pr._addToLog);
        });
    });

    describe('print function', ()=>{
        it('print the into the example', ()=>{
            assert.deepEqual(pr.print(), 'id|name|position\n0|Nancy|architect');
        });
    });

    describe('addEntries function', ()=>{
        it('return "Entries added!"',()=>{
            assert.deepEqual(pr.addEntries('Edd:administrator'), "Entries added!");
        });

        it('add to data', ()=>{
            pr.addEntries('Edd:administrator');
            assert.deepEqual(pr.data, [ { Nancy: 'architect' }, { Edd: 'administrator' } ]);
        })
    });

    describe('removeEntry function', ()=>{
        it('if entry exist remove it and return message', ()=>{
            pr.addEntries('Edd:administrator');
            assert.deepEqual(pr.removeEntry('Edd'), "Removed correctly!");
        });

        it('if entry dose not exist throw an error', ()=>{
            assert.throw(()=> pr.removeEntry('Edd'), "There is no such entry!");
        });

        it('if entry exist remove it from data', ()=>{
            pr.addEntries('Edd:administrator');
            pr.removeEntry('Edd')
            assert.deepEqual(pr.data, [ { Nancy: 'architect' } ]);
        });
    });
});