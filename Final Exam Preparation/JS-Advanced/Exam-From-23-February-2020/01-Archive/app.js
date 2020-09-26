function solve(){
   let createButton = document.querySelector('form button');
   let authorInput = document.getElementById('creator');
   let titleInput = document.getElementById('title');
   let categoryInput = document.getElementById('category');
   let contentInput = document.getElementById('content');
   let sections = document.getElementsByTagName('section');
   let archiveUl = document.querySelector('.archive-section ul');
   let arrayList = [];

   createButton.addEventListener('click', createHandler);
   sections[1].addEventListener('click', deleteAndArchiveHandler);

   function deleteAndArchiveHandler(e){
      if(e.target.textContent === 'Archive'){
         for (const iterator of arrayList) {
            archiveUl.removeChild(iterator);
         }
         let li = document.createElement('li');
         li.textContent = e.target.parentElement.previousSibling.previousSibling.previousSibling.previousSibling.textContent;
         arrayList.push(li);
         arrayList.sort((a,b) =>{
            return a.textContent.localeCompare(b.textContent)
         });

         for (const iterator of arrayList) {
            archiveUl.appendChild(iterator);
         }
         e.target.parentElement.parentElement.remove();
      } else if(e.target.textContent === 'Delete'){
         e.target.parentElement.parentElement.remove();
      }
   }

   function createHandler(el){
      el.preventDefault();
      
      let h1Title = document.createElement('h1');
      h1Title.textContent = titleInput.value;
      let pCategory = document.createElement('p');
      pCategory.textContent = "Category: ";
      let strongCategory = document.createElement('strong');
      strongCategory.textContent = categoryInput.value;
      pCategory.appendChild(strongCategory);
      let pCreator = document.createElement('p');
      pCreator.textContent = "Creator: ";
      let strongCreator = document.createElement('strong');
      strongCreator.textContent = authorInput.value;
      pCreator.appendChild(strongCreator);
      let pContent = document.createElement('p');
      pContent.textContent = contentInput.value;
      let div = document.createElement('div');
      div.className = 'buttons';
      let deleteButton = document.createElement('button');
      deleteButton.classList.add('btn', 'delete');
      deleteButton.textContent = 'Delete';
      let archiveButton = document.createElement('button');
      archiveButton.classList.add('btn', 'archive');
      archiveButton.textContent = "Archive";
      div.appendChild(deleteButton);
      div.appendChild(archiveButton);
      let article = document.createElement('article');
      article.appendChild(h1Title);
      article.appendChild(pCategory);
      article.appendChild(pCreator);
      article.appendChild(pContent);
      article.appendChild(div);
      sections[1].appendChild(article);
   }
}
