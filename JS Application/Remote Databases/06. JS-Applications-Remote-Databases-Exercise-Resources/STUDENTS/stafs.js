export function values(id, firstName, lastName, facultyNumber, grade){
    return {
        id: id.value,
        firstName: firstName.value,
        lastName: lastName.value,
        facultyNumber: facultyNumber.value,
        grade: grade.value
    };
}

export function isDataValid(id, firstName, lastName, facultyNumber, grade, allIds, h4, form){
    if(id.value === '' || firstName.value === '' || lastName.value === '' || facultyNumber.value === '' 
    || grade.value === ''){
        h4.textContent = "Please fill the empty inputs!";
        form.appendChild(h4);
        throw new Error("Please fill the empty inputs!");
    } else if(Number(id.value) === NaN) {
        h4.textContent = 'Id must be number!';
        form.appendChild(h4);
        throw new Errort('Id must be number!');
    } else if(typeof firstName.value !== 'string') {
        h4.textContent = 'First Name must be string!';
        form.appendChild(h4);
        throw new Error('First Name must be string!');
    } else if(typeof lastName.value !== 'string') {
        h4.textContent = 'Last Name must be string!';
        form.appendChild(h4);
        throw new Error('Last Name must be string!');
    } else if(Number(facultyNumber.value) === NaN) {
        h4.textContent = 'Faculty Number must be number!';
        form.appendChild(h4);
        throw new Error('Faculty Number must be number!');
    } else if(Number(grade.value) === NaN) {
        h4.textContent = 'Grade must be number!';
        form.appendChild(h4);
        throw new Errort('Grade must be number!');
    } else if(allIds.includes(id.value.toString())){
        h4.textContent = 'This Id is already used!';
        form.appendChild(h4);
        throw new Error('This Id is already used!');
    } else {
        return false;
    }

    return true;
}

export function fillTable(output, table, allStudents, allIds){
        for (const key in output) {
            allStudents.push(output[key]);
            allIds.push(output[key].id);
        }

        allStudents.sort((a, b) => a.id - b.id);
        
        allStudents.forEach(student => {
            let tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${student.id}</td>
                <td>${student.firstName}</td>
                <td>${student.lastName}</td>
                <td>${student.facultyNumber}</td>
                <td>${student.grade}</td>
            `
            table.appendChild(tr);
        });
}