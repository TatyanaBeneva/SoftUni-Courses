export default function callAndRedirectNotifications(list, message, context, link){
    const section = document.querySelectorAll('section')[list];
    const paragraph = section.children[0];
    paragraph.textContent = message;
    section.style.display = 'block';
    setTimeout(()=>{
        section.style.display = 'none';
        context.redirect(link);
    }, 2000);
}