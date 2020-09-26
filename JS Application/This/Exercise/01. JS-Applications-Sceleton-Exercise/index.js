function solve(){
   let tbody = document.querySelector('tbody');

   tbody.addEventListener('click', (e)=>{           
      let tr = Array.from(tbody.querySelectorAll('tr'));
      for(let i = 0; i < tr.length; i++){
         tr[i].style.backgroundColor = '';
         if(e.target.parentElement === tr[i]){
            e.target.parentElement.style = 'background-color: #413f5e';
         }
      }
   })
}
