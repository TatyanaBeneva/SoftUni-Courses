import models from "../models/index.js";
import extend from '../utils/helper.js';

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
                context.redirect('#/login');
            })
        }
    },

    post: {
        login(context){
            const { email, password} = context.params;

            models.user.login(email, password)
                .then((response) => {
                    context.redirect('#/home');
                })
                .catch((e) => {
                    console.error(e);                    
                });
        },

        register(context){
            const { email, password, repeatPassword } = context.params;

            if (password === repeatPassword) {
                models.user.register(email, password)
                    .then((response) => {
                        context.redirect('#/login');
                    })
                    .catch((e) => {
                        console.error(e);
                    })
            }
        }
    }
}
