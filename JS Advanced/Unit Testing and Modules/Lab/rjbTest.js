let assert = require('chai').assert;
let rgbToHexColor = require('./rjb').rgbToHexColor;

describe('validate the colors', () =>{
    it('validate red rgb color', () =>{
        assert.equal(rgbToHexColor(-2,21,56), undefined, 'red value is invalide');
    });

    it('validate red rgb color', () =>{
        assert.equal(rgbToHexColor(270,21,56), undefined, 'red value is invalide');
    });

    it('validate red rgb color', () =>{
        assert.equal(rgbToHexColor(32.8,21,56), undefined, 'red value is invalide');
    });

    it('validate green rgb color', () =>{
        assert.equal(rgbToHexColor(80,-98,56), undefined, 'green value is invalide');
    });

    it('validate green rgb color', () =>{
        assert.equal(rgbToHexColor(80,300,56), undefined, 'green value is invalide');
    });

    it('validate green rgb color', () =>{
        assert.equal(rgbToHexColor(80,60.5,56), undefined, 'green value is invalide');
    });

    it('validate blue rgb color', () =>{
        assert.equal(rgbToHexColor(80,-25,56), undefined, 'blue value is invalide');
    });

    it('validate blue rgb color', () =>{
        assert.equal(rgbToHexColor(80,265,56), undefined, 'blue value is invalide');
    });

    it('validate blue rgb color', () =>{
        assert.equal(rgbToHexColor(80,60.5,56), undefined, 'blue value is invalide');
    });

    it('validate blue rgb color', () =>{
        assert.equal(rgbToHexColor(21,56), undefined, 'blue value is missing');
    });

    it('validate rgb color to hexadecimal', () =>{
        assert.equal(rgbToHexColor(250,128,114), '#FA8072', 'rgb colors should return #FA8072');
    });

    it('if input is empty', () =>{
        assert.equal(rgbToHexColor(), undefined, 'empty input');
    });

    it('should return #FFA07A', () =>{
        assert.equal(rgbToHexColor(255,160,122), '#FFA07A');
    });

    it('should return  #FFFFFF', () =>{
        assert.equal(rgbToHexColor(255,255,255), '#FFFFFF');
    });

    it('should return  #000000', () =>{
        assert.equal(rgbToHexColor(0,0,0), '#000000');
    });
});