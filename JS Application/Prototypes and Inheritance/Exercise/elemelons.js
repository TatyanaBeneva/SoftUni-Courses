(()=>{
    class Melon {
        constructor(weight, melonSort){
            this.weight = weight;
            this.melonSort = melonSort;
            this.element = '';
        }

        getElementIndex(){
            return this.weight * this.melonSort.length;
        }

        toString(){
            return `Element: ${this.element}\nSort: ${this.melonSort}\nElement Index: ${this.getElementIndex}`
        }
    }

    class Watermelon extends Melon{
        constructor(weight, melonSort){
            super(weight, melonSort);
            this.element = 'Water';
        }
    }

    class Firemelon extends Melon{
        constructor(weight, melonSort){
            super(weight, melonSort);
            this.element = 'Fire';
        }
    }

    class Earthmelon extends Melon{
        constructor(weight, melonSort){
            super(weight, melonSort);
            this.element = 'Earth';
        }
    }

    class Airmelon extends Melon{
        constructor(weight, melonSort){
            super(weight, melonSort);
            this.element = 'Air';
        }
    }

    class Melolemonmelon extends Watermelon{
        constructor(weight, melonSort){
            super(weight, melonSort);
            this.element = ['Fire', 'Earth', 'Air','Water'];
            this.element = 'Water';
        }

        morph(){
            let nextElement = this.element.shift();
            this.element = nextElement;
            this.element.push(nextElement);
        }
    }

    return {
        Melon,
        Watermelon,
        Firemelon,
        Earthmelon,
        Airmelon,
        Melolemonmelon
    }
})