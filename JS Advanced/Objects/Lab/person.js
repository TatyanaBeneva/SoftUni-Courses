class Person {
    constructor(firstName, lastName, age, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = Number(age);
        this.email = email;
    }

    returnThis(){
        return this;
    }

    toString(){
        return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`;
    }
};


function getPersons(){
    const array = [];
    let per = new Person();
    for(let i = 0; i < Person.length; i++){
        array.push(returnThis());
    }

    return array;
}


let persons = getPersons();
console.log(persons);
