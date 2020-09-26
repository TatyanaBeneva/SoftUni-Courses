function solve() {
    let buttonDropdown = document.getElementById('dropdown');
    let dropdownUl = document.getElementById('dropdown-ul');
    let box = document.getElementById('box');

    buttonDropdown.addEventListener('click', (e)=>{       
        if(dropdownUl.style.display === "none"){
            dropdownUl.style.display = "block";
        } else{
            dropdownUl.style.display = "none";
            box.style.backgroundColor = "black";
        }
    });

    dropdownUl.addEventListener('click', (e)=>{       
        box.style.backgroundColor = e.target.textContent;
    })

}