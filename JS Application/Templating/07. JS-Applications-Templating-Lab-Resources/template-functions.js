import {contacts} from './contacts.js';

(async () => {
    Handlebars.registerPartial('contact', await fetch('./contact-template.hbs').then(r => r.text()));
    const template = Handlebars.compile(await fetch('./contacts-template.hbs').then(r => r.text()));

    const resultHTML = template({contacts});

    document.querySelector('body').innerHTML += resultHTML;

    document.querySelectorAll('button').forEach(btn => {
        btn.addEventListener('click', () => {
            const parent = btn.parentElement;
            const divDetails = parent.querySelector('div.details');
            const {display} = divDetails.style;

            if(display === 'none'){
                divDetails.style.display = 'block';
            } else{
                divDetails.style.display = 'none';
            }
        })
    })
})();