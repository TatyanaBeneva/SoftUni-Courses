let assert = require('chai').assert;
let lookupChar = require('./charLookup').lookupChar;

describe('lookupChar() behavior', () =>{
    it('with numbers arg', () =>{
        assert.equal(lookupChar(5,5), undefined);
    });

    it('with string and object arg', () =>{
        assert.equal(lookupChar('some text', {}), undefined);
    });

    it('invalid index range', () =>{
        assert.equal(lookupChar('some text', 200), 'Incorrect index');
    });

    it('invalid index range', () =>{
        assert.equal(lookupChar('some text', -10), 'Incorrect index');
    });

    it('with valid arg', () =>{
        assert.equal(lookupChar('some text', 3), 'e');
    });

    it('is index integer', () =>{
        assert.equal(lookupChar('some text', 2.5), undefined);
    });
});