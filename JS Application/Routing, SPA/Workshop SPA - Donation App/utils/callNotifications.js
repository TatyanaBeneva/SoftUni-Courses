export default function callAndRedirectNotifications(divId, message, context, link){
    const divSuccess = document.querySelector(divId);
    divSuccess.textContent = message;
    divSuccess.style.display = 'block';
    setTimeout(()=>{
        divSuccess.style.display = 'none';
        context.redirect(link);
    }, 2000);
}