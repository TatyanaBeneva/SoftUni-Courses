const stringBuilder = require('./stringBuilder');

let assert = require('chai').assert;
let StringBuilder = require('./stringBuilder').StringBuilder;

describe('StringBulder class behavior', () =>{
    let sb;

    beforeEach(function(){
        sb = new StringBuilder();
    })

    describe('constructor check', () =>{
        it('without param', () =>{
            assert.deepEqual(new StringBuilder()._stringArray, []);
        });

        it('with param', () =>{
            assert.deepEqual(new StringBuilder('some')._stringArray, ['s','o','m','e']);
        });

        it('with param boolean', () =>{
            assert.throw(() => new StringBuilder(true), 'Argument must be string');
        });

        it('with param number', () =>{
            assert.throw(() => new StringBuilder(199.5), 'Argument must be string');
        });
    });

    describe('append method', () =>{
        it('with valid string', () =>{
            sb.append('123');
            assert.deepEqual(sb._stringArray, ['1','2','3']);
        });

        it('with string plus string', () =>{
            sb = new StringBuilder('123');
            sb.append('44');
            assert.deepEqual(sb._stringArray, ['1','2','3','4','4']);
        });

        it('with invalid args', () =>{
            assert.throw(() => sb.append(5), 'Argument must be string');
        });
    });

    describe('remove method', () =>{
        it('with valid args', () =>{
            sb = new StringBuilder('1234567');
            sb.remove(0, 3);
            assert.deepEqual(sb._stringArray, ['4','5','6','7']);
        });

        it('with invalid args', () =>{
            sb = new StringBuilder('123');
            assert.deepEqual(sb.remove('123'), undefined);
        });
    });

    describe('prepend method', () =>{
        it('with valid data string', () =>{
            sb = new StringBuilder('ab');
            sb.prepend('dd');
            assert.deepEqual(sb._stringArray, ['d','d','a','b']);
        });

        it('with invalid data', () =>{            
            assert.throw(() => sb.prepend([]), 'Argument must be string');
        });
    });

    describe('insertAt method', () =>{
        it('with valid data string', () =>{
            sb = new StringBuilder('asd');
            sb.insertAt('9', 1);
            assert.deepEqual(sb._stringArray, ['a','9','s','d']);
        });

        it('throw an error', () =>{            
            assert.throw(() => sb.insertAt(9,2), 'Argument must be string');
        });

        it('with invalid data', () =>{            
            assert.equal(sb.insertAt('text', 'text'), undefined);
        });

    });

    describe('toString method', () =>{
        it('with empty array', () =>{
            let actresult = sb.toString();
            let expresult = "";
            assert.equal(actresult, expresult);
        });

        it('with not empty array', () =>{            
            sb = new StringBuilder('123');
            sb.append('4');
            sb.remove(0,2);
            assert.equal(sb.toString(), '34');
        });

        it('is return', () =>{            
            sb = new StringBuilder('123');
            sb.append('4');
            sb.remove(0,2);
            assert.isOk(sb.toString());
        });

        it('throw an error',() =>{
            assert.throw(() => new StringBuilder(78), 'Argument must be string');
        });
    });

    it('with all methods', () =>{
        sb = new StringBuilder('hello');
        sb.append(', there');
        sb.prepend('User, ');
        sb.insertAt('woop',5 );
        sb.remove(6, 3);
        assert.equal(sb.toString(), 'User,w hello, there');
    });

    it('throw error on the static method', () =>{
        assert.throw(() => StringBuilder._vrfyParam(124), 'Argument must be string');
    });
});