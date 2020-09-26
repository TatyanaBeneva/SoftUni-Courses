let assert = require('chai').assert;
let createCalculator = require('./add').createCalculator;

describe('create calculator', () =>{
    let calc;

    beforeEach(function () {
        calc = createCalculator();
    });

    it('should return 0 for get', () =>{       
        let value = calc.get();
        assert.equal(value, 0);
    });

    it('should return 10 for add(3) and add(7)', () =>{
        calc.add(3);
        calc.add(7);
        let value = calc.get();
        assert.equal(value, 10);
    });

    it('should return -4 for add("3") and add("7") and substract(14)', () =>{
        calc.add("3");
        calc.add("7");
        calc.subtract(14)
        let value = calc.get();
        assert.equal(value, -4);
    });

    it('should return -10 for substract(3) and substract(7)', () =>{
        calc.subtract(3);
        calc.subtract(7);
        let value = calc.get();
        assert.equal(value, -10);
    });

    it('should return NaN for add(string)', () =>{
        calc.add('string')
        let value = calc.get();
        assert.isNaN(value);
    });

    it('should return NaN for substract(string)', () =>{
        calc.subtract('string')
        let value = calc.get();
        assert.isNaN(value);
    });
});