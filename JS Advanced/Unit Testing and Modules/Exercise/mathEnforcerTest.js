let assert = require('chai').assert;
let mathEnforcer = require('./mathEnforcer').mathEnforcer;

describe('mathEnforcer behavior', () =>{
    describe('addFive()', () =>{
        it('with invalid arg', ()=>{
            assert.equal(mathEnforcer.addFive([1,2,3]), undefined);
        });

        it('with valid arg', ()=>{
            assert.equal(mathEnforcer.addFive(9), 14);
        });

        it('with negative arg', ()=>{
            assert.equal(mathEnforcer.addFive(-10), -5);
        });

        it('with floating point arg', ()=>{
            assert.equal(mathEnforcer.addFive(15.5), 20.5);
        });
    });

    describe('substractTen()', () =>{
        it('with invalid arg', ()=>{
            assert.equal(mathEnforcer.subtractTen('dadas'), undefined);
        });

        it('with valid arg', ()=>{
            assert.equal(mathEnforcer.subtractTen(14), 4);
        });

        it('with negative arg', ()=>{
            assert.equal(mathEnforcer.subtractTen(-14), -24);
        });

        it('with floating point arg', ()=>{
            assert.equal(mathEnforcer.subtractTen(15.9), 5.9);
        });
    });

    describe('sum()', () =>{
        it('with invalid first arg', ()=>{
            assert.equal(mathEnforcer.sum('123', 9), undefined);
        });

        it('with invalid second arg', ()=>{
            assert.equal(mathEnforcer.sum(19, ['123', 2]), undefined);
        });

        it('with valid arg', ()=>{
            assert.equal(mathEnforcer.sum(100, 9.5), 109.5);
        });

        it('with negative arg', ()=>{
            assert.equal(mathEnforcer.sum(-50, 100), 50);
        });

        it('with floating point arg', ()=>{
            assert.equal(mathEnforcer.sum(50.9,100), 150.9);
        });

        it('with negative and floating point arg', ()=>{
            assert.equal(mathEnforcer.sum(-50, 10.5), -39.5);
        });
    });
});