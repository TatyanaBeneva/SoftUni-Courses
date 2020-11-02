import {getStudents, postStudents} from './firebaseRequest.js';
import {values, fillTable, isDataValid} from './stafs.js';

(function doStaff() {
    let id = document.getElementById('id');
    let firstName =  document.getElementById('firstName')
    let lastName =  document.getElementById('lastName');
    let facultyNumber = document.getElementById('facultyNumber');
    let grade = document.getElementById('grade');
    let form = document.querySelector('form');
    let table = document.querySelector('#results > tbody');
    let h4 = document.createElement('h4');
    let allIds = [];

    form.addEventListener('submit', async (e) => {       
        e.preventDefault();
        let allStudents = [] 
        if(isDataValid(id, firstName, lastName, facultyNumber, grade, allIds, h4, form) === false){
            await postStudents(values(id, firstName, lastName, facultyNumber, grade));
            h4.remove();
            table.innerHTML = '';
            await getStudents()
            .then(output => fillTable(output, table, allStudents, allIds));
            erasedInputs()
        }
        console.log(allIds);    
    });

    function erasedInputs(){
        id.value = '';
        firstName.value ='';
        lastName.value = '';
        facultyNumber.value = '';
        grade.value = '';
    }
})();
