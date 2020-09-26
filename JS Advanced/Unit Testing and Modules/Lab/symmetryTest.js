let assert = require('chai').assert;
let isSymmetric = require('./symmetry').isSymmetric;

describe('check for symmertry of an Array', () =>{
    it('check if the input is array of strings', () =>{
        let input = ['fds','das','daa'];
        assert.isArray(input, 'should return true for array of strings');
    });

    it('check if the input is array of numbers', () =>{
        let input = [1,3,5,7];
        assert.isArray(input, 'should return true for array of numbers');
    });

    it('check if the input is array with one value', () =>{
        let input = [2];
        assert.isArray(input, 'should return true for array with one value');
    });

    it('check if the input is not an array with input number', () =>{
        let input = 45;
        assert.isNotArray(input, 'should return false for not array');
    })

    it('check if the input is not an array with input string', () =>{
        let input = 'fgfh';
        assert.isNotArray(input, 'should return false for not array');
    })
    
    it('check if the input is reverse', () =>{
        let input = [1, 4, 'fssd', 4, 1];
        assert.equal(isSymmetric(input), true, 'should return true');
    })

    it('check if the input is reverse', () =>{
        let input = [1, 3, 'fssd', 4, 1];
        assert.equal(isSymmetric(input), false, 'should return true');
    })

    it('if input is not array', () =>{
        assert.equal(isSymmetric(1,2,2,1), false, 'should return false, not array');
    })

    it('if input is not symmetry', () =>{
        assert.equal(isSymmetric([5,'hi',{a:5},new Date(),{a:5},'hi',5]), true);
    })
});
