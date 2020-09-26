function solve() {
   let searchButton = document.getElementById('searchBtn');
   let input = document.getElementById('searchField');
   let dataTr = Array.from(document.querySelectorAll('tbody > tr'));

   

   searchButton.addEventListener('click', (e) =>{

      let regex = new RegExp(input.value, 'gim');

      dataTr.map(e => {
         e.classList.remove('select');

         if(e.innerHTML.match(regex) !== null){
            e.className = 'select';
         }
      });

      input.value = '';
   })
}