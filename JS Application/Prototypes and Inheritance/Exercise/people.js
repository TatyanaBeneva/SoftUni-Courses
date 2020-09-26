(()=>{
    class Employee {
        constructor(name, age){
            this.name = name;
            this.age = age;
            this.salary = 0;
            this.tasks = [];
        }

        work(){
            let task = this.tasks.shift();
            console.log(this.name + task);
            this.tasks.push(task);
        }

        collectSalary(){
            console.log(`${this.name} received ${this.salary} this month.`);
        }
    }

    class Junior extends Employee{
        constructor(name, age){
            super(name, age);
            this.tasks = [" is working on a simple task."];
        }
    }

    class Senior extends Employee {
        constructor(name, age){
            super(name, age);
            this.tasks = [
                " is working on a complicated task.",
                " is taking time off work.",
                " is supervising junior workers."
            ];
        }
    }

    class Manager extends Employee{
        constructor(name, age){
            super(name, age);
            this.dividend = 0;
            this.tasks.push(" scheduled a meeting.");
            this.tasks.push(" is preparing a quarterly report.");
        }

        getSalary(){
            return this.salary + this.dividend;
        }

        collectSalary(){
            console.log(`${this.name} received ${this.getSalary()} this month.`);
        }
    }

    return {
        Employee,
        Junior,
        Senior,
        Manager
    }
})