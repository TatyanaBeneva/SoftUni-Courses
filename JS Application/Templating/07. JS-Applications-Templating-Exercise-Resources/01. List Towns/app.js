
const elements = {
    loadBtn: document.getElementById('btnLoadTowns'),
    root: document.getElementById('root')
}

elements.loadBtn.addEventListener('click', e => {
    Promise.all([
        fetch('https://restcountries.eu/rest/v2/all').then(r => r.json()),
        fetch('./template.hbs').then(r => r.text())
    ])
    .then(([countries, templateHbs]) => {
        const template = Handlebars.compile(templateHbs);
        const resultHTML = template({countries});
        elements.root.innerHTML = resultHTML;
    })
})