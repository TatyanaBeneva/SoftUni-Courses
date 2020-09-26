let assert = require('chai').assert;
let isOddOrEven = require('./oddOrEven').isOddOrEven;

describe('isOddOrEven() behavior', () =>{
    it('check the type of the input', () =>{
        assert.equal(isOddOrEven(false), undefined);
    });

    it('check the type of the input', () =>{
        assert.equal(isOddOrEven(15), undefined);
    });

    it('check the string - even case', () =>{
        assert.equal(isOddOrEven('testingg'), 'even');
    });

    it('check the string - odd case', () =>{
        assert.equal(isOddOrEven('testing'), 'odd');
    });
});