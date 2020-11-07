(async() => {
    Handlebars.registerPartial('cat', await fetch('./single-cat-template.hbs').then(r => r.text()));
    const template = Handlebars.compile(await fetch('./all-cats-template.hbs').then(r => r.text()));
    const resultHTML = template({cats});
    document.querySelector('section#allCats').innerHTML += resultHTML;
    document.querySelectorAll('button').forEach(btn => {
        btn.addEventListener('click', () => {
            const parent = btn.parentElement;
            const statusDiv = parent.querySelector('div.status');
            const {display} = statusDiv.style;

            if(display === 'none'){
                btn.textContent = 'Hide status code';
                statusDiv.style.display = 'block';
            } else{
                btn.textContent = 'Show status code';
                statusDiv.style.display = 'none';
            }
        })
    })
})();
