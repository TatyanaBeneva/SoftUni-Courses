export default function (context) {
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            // User is signed in.
            context.isLoggedIn = true;
            context.username = user.email;
            context.userId = user.uid;
            localStorage.setItem('email', user.email);
            localStorage.setItem('userId', user.uid);
        } else {
            // User is signed out.
            context.isLoggedIn = false;
            context.username = null;
            context.userId = null;
            localStorage.clear();
        }
    });

    return context.loadPartials({
        notifications: '../Views/Common/notifications.hbs',
        header: '../Views/Common/header.hbs',   
        footer: '../Views/Common/footer.hbs'
    });

}