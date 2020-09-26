function createArticle() {
	let title = document.getElementById('createTitle').value;
	let header3 = document.createElement('h3');
	header3.textContent = title;
	let contentText = document.getElementById('createContent').value;
	let pharagraph = document.createElement('p');
	pharagraph.textContent = contentText;
	let article = document.createElement('article');

	if(title.length > 0 && contentText.length > 0){
		document.getElementById('articles').appendChild(article);
		article.appendChild(header3);
		article.appendChild(pharagraph);
		document.getElementById('createTitle').value = '';
		document.getElementById('createContent').value = '';
	}
}