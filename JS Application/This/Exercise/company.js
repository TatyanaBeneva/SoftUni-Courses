class Company{
    constructor(){
        this.departments = [];
    }

    addEmployee(username, salary, position, department){
        if(!username || (!salary && salary !== 0) || !position || !department){
            throw new Error('Invalid input!');
        }

        if(salary < 0){
            throw new Error('Invalid input!');
        }

        let found = false;
        for(let i = 0; i < this.departments.length; i++){
            if(this.departments[i].department === department){
                found = true;
                break;
            }
        }
        if(found){
            this.departments.map(x => {
                if(x.department === department){
                    x.data.push({username, salary, position})
                    x.totalSalary += salary;
                    x.id++;
                }
            });
        } else{
            this.departments.push({department, data: [{username, salary, position}], totalSalary: salary, id: 1});
        }

        return `New epmloyee is hired. Name: ${username}. Position: ${position}`;
    }

    bestDepartment(){
        this.departments.map(x => {
            let avg = x.totalSalary / x.id;
            x.avgSalary = avg;
        });
        this.departments.sort((a,b) => {
            return b.avgSalary - a.avgSalary;
        })

        let result = [];

        this.departments[0].data.sort((a,b) =>{
            if(a.salary !== b.salary){
                return b.salary - a.salary;
            }

            return a.username.localeCompare(b.username);
        })
        result.push(`Best department is: ${this.departments[0].department}`);
        result.push(`Average salary: ${this.departments[0].avgSalary}`);
        for (const iterator of this.departments[0].data) {
            result.push(`${iterator.username} ${iterator.salary} ${iterator.position}`);
        }

        return result.join('\n');
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
