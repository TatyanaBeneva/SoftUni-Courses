
(() => {
        class Figure{
        changeMulti;
        constructor(type){
            this.type = type;

            if(this.type === undefined){
                this.type = 'cm';
                this.changeMulti = 1;
                this.multi = 1;
            } else if(this.type === 'mm'){
                this.multi = 10;
            } else if(this.type === 'm'){
                this.multi = 0.1;
            }
        }

        changeUnits(typeOfValue){
            if(typeOfValue === 'mm' && this.type === 'cm'){
                this.type = 'mm';
                return this.multi = 10;
            } else if(typeOfValue === 'm' && this.type === 'cm'){
                this.type = 'm';
                return this.multi = 0.1;
            } else if(typeOfValue === 'm' && this.type === 'mm'){
                this.type = 'm';
                return this.multi = 0.01;
            } else if(typeOfValue === 'mm' && this.type === 'm'){
                this.type = 'mm';
                return this.multi = 100;
            } else if(typeOfValue === 'cm' && this.type === 'm'){
                this.type = 'cm';
                return this.multi = 10;
            } else if(typeOfValue === 'cm' && this.type === 'mm'){
                this.type = 'cm';
                return this.multi = 0.1;
            }
        }
    }

    class Circle extends Figure{
        constructor(radius, type){
            super(type);
            this.radius = radius * this.multi;
        }

        get area(){
            return Math.PI * (this.radius) * (this.radius);
        }

        toString(){
            return `Figures units: ${this.type} Area: ${this.area} - radius: ${this.radius}`;
        }
    }

    class Rectangle extends Figure{
        constructor(width, height, type){
            super(type);
            if(this.type === 'cm'){
                this.width = width;
                this.height = height;
            } else if(this.type === 'mm'){
                this.width = width * 10;
                this.height = height * 10;
            } else if(this.type === 'm'){
                this.width = width * 0.1;
                this.height = height * 0.1;
            }
        }

        get area(){
            return this.width * this.height;
        }

        toString(){
            return `Figures units: ${this.type} Area: ${this.area} - width: ${this.width}, height: ${this.height}`;
        }
    }

    return {Figure, Rectangle, Circle}

});


let c = new Circle(5);
console.log(c.area); // 78.53981633974483
console.log(c.toString()); // Figures units: cm Area: 78.53981633974483 - radius: 5

let r = new Rectangle(3, 4, 'mm');
console.log(r.area); // 1200 
console.log(r.toString()); //Figures units: mm Area: 1200 - width: 30, height: 40

r.changeUnits('cm');
console.log(r.area); // 12
console.log(r.toString()); // Figures units: cm Area: 12 - width: 3, height: 4

c.changeUnits('mm');
console.log(c.area); // 7853.981633974483
console.log(c.toString()) // Figures units: mm Area: 7853.981633974483 - radius: 50
