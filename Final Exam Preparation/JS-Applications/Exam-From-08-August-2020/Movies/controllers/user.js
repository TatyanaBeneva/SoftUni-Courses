import models from "../models/index.js";
import extend from '../utils/helper.js';
import notification from '../utils/callNotifications.js';

export default {
    get: {
        login(context){
            extend(context).then(function () {
                this.partial('../Views/Login/login.hbs');
            })
        },

        register(context){
            extend(context).then(function () {
                this.partial('../Views/Register/register.hbs');
            })
        },

        logout(context){
            models.user.logout().then((response) => {
                notification(1, "Successful logout" , context, '#/user/login');
            })
        }
    },

    post: {
        login(context){
            const { email, password, repeatPassword } = context.params;

            models.user.login(email, password)
                .then((response) => {
                    notification(1, "Login successful.", context, '#/home');
                })
                .catch((e) => {
                    console.error(e);                    
                    notification(0, "Incorect email or password!", context);
                });
        },

        register(context){
            const { email, password, repeatPassword } = context.params;

            if (password === repeatPassword) {
                models.user.register(email, password)
                    .then((response) => {
                        notification(1, "Successful registration!", context, '#/home');
                    })
                    .catch((e) => {
                        console.error(e);
                        notification(0, "Incorrect email or password!", context);
                    })
            } else{
                notification(0, "Both passwords must be the same!", context);
            }
        }
    }
}
