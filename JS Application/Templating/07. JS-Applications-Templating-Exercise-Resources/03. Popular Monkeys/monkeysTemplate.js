import { monkeys } from './monkeys.js';

(async () => {
    Handlebars.registerPartial('monkey', await fetch('./monkey-template.hbs').then(r => r.text()));
    let templateSrc = await fetch('./monkeys-template.hbs').then(r => r.text());
    let template = Handlebars.compile(templateSrc);
    let resultHTML = template({monkeys});
    document.querySelector('section').innerHTML += resultHTML;
    document.querySelectorAll('button').forEach(btn => {
        btn.addEventListener('click', () => {
            const parent = btn.parentElement;
            const pInfo = parent.querySelector('p');
            const {display} = pInfo.style;

            if(display === 'none'){
                pInfo.style.display = 'block';
            } else{
                pInfo.style.display = 'none';
            }
        })
    })
})();