function Person(firstName, lastName){
    this.first = firstName;
    this.last = lastName;
    Object.defineProperties(this, {
           "firstName": {
           get: function() { return this.first; },
           set: function(name) { this.first = name; }
        },
            "lastName": {
           get: function() { return this.last; },
           set: function(name) { this.last = name; }
        },
            "fullName": {
            get: function () { return this.first + ' ' + this.last },
            set: function (name) {
              var parts = name.split(' ')
              this.first = parts[0];
              this.last = parts[1];
            }
        }
    });
   
}

let person = new Person("Peter", "Ivanov");
console.log(person.fullName);//Peter Ivanov
person.firstName = "George";
console.log(person.fullName);//George Ivanov
person.lastName = "Peterson";
console.log(person.fullName);//George Peterson
person.fullName = "Nikola Tesla";
console.log(person.firstName)//Nikola
console.log(person.lastName)//Tesla
