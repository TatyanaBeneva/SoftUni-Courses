import {apiKey, createNewBook, getAllBooks, getBookById, updateBook, deleteBook, patchBook} from './firebaseRequests.js';
function extractFormData(formRef, formConfig){
    return formConfig.reduce((acc, inputName) => {
        acc[inputName] = formRef.elements[inputName].value;
        return acc;
    }, {});
}

function fillFormWithData(formRef, formValue){
    Object.entries(formValue).map(([inputName, value]) => {
        formRef.elements.namedItem(inputName).value = value;
    });
}

function addTableRow(tBody, bookValue, bookId){
    let tempRow = document.createElement('tr');
    tempRow.setAttribute('data-book-id', bookId);
    tempRow.innerHTML = `
    <td>${bookValue.title}</td>
    <td>${bookValue.author}</td>
    <td>${bookValue.isbn}</td>
    <td>${bookValue.tags}</td>
    <td>
        <button data-method="edit">Edit</button>
        <button data-method="delete">Delete</button>
    </td>
    `;

    tBody.appendChild(tempRow);
}

(function doStuff(){
    let formInputs = ['title', 'author', 'isbn'];
    let formRef = document.querySelector('form')
    let tagFormRef= document.getElementById('tagForm');
    let tBodyRef = document.querySelector('tbody');
    let loadBooksButtonRef = document.getElementById('loadBooks');
    let titleInp = document.getElementById('title');
    let authorInp = document.getElementById('author');
    let isbnInp = document.getElementById('isbn');
    let tagInputs = ['tags'];

    function showAllBooks(tBodyRef){
        getAllBooks().then(resp => {
            tBodyRef.innerHTML = '';
            Object.entries(resp).map(([id, bookValue]) => {
                addTableRow(tBodyRef, bookValue, id);
            })
        })
    }

    let lastSelectedBook = '';

    tagFormRef.addEventListener('submit', e => {
        e.preventDefault();
        let parsedForm = extractFormData(tagFormRef, tagInputs);
        patchBook(parsedForm, lastSelectedBook);
        document.getElementById('tags').value = '';
    })

    formRef.addEventListener('submit', e => {
        e.preventDefault();
        let parsedForm = extractFormData(formRef, formInputs);

        createNewBook(parsedForm);

        titleInp.value = '';
        authorInp.value = '';
        isbnInp.value = '';
    });

    loadBooksButtonRef.addEventListener('click', () =>{
        // getAllBooks().then(resp => {
        //     tBodyRef.innerHTML = '';
        //     Object.entries(resp).map(([id, bookValue]) => {
        //         addTableRow(tBodyRef, bookValue, id);
        //     })
        // })

        showAllBooks(tBodyRef);
    });

    tBodyRef.addEventListener('click', async (e) =>{
        let targetBookId = e.target.closest('tr').dataset.bookId;

        if(e.target instanceof HTMLButtonElement){
            const method = e.target.dataset.method;

            if(method === 'edit'){
                await updateBook(extractFormData(formRef, formInputs), targetBookId);
            }

            if(method === 'delete'){
                await deleteBook(targetBookId);
            }

            showAllBooks(tBodyRef);

            return;
        }
        lastSelectedBook = targetBookId;
        getBookById(targetBookId).then(x => {
            fillFormWithData(formRef, x);
        });
    })
    console.log(apiKey);
})();