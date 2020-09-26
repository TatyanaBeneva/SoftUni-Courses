function create(words) {
   for (const word of words) {
        let div = document.createElement('div');
        let paragraph = document.createElement('p');
        paragraph.textContent = word;
        paragraph.style.display = 'none';
        div.appendChild(paragraph);

        div.addEventListener('click', (e) =>{
            paragraph.style.display = 'block';
        })

        let content = document.getElementById('content');
        content.appendChild(div);

   }

}