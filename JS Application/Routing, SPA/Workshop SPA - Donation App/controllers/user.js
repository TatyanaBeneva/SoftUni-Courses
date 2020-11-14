import models from "../models/index.js";
import extend from '../utils/helper.js';
import notification from '../utils/callNotifications.js';

export default {
    get: {
        login(context) {
            extend(context).then(function () {
                this.partial('../views/user/login.hbs');
            })
        },
        register(context) {
            extend(context).then(function () {
                this.partial('../views/user/register.hbs');
            })
        },
        logout(context) {
            models.user.logout().then((response) => {
                notification('#successNotification', "You logout successfully!", context, '#/home');
            })
        }
    },

    post: {
        login(context) {
            const { username, password, rePassword } = context.params;
            const divLoading = document.querySelector('#loadingNotification');
            divLoading.style.display = 'block';

            models.user.login(username, password)
                .then((response) => {
                    divLoading.style.display = 'none';
                    notification('#successNotification', "You logged in successfully!", context, '#/home');
                })
                .catch((e) => {
                    divLoading.style.display = 'none';
                    console.error(e);                    
                    notification('#errorNotification', "Incorect email or password!", context);
                });
        },
        register(context) {
            const { username, password, rePassword } = context.params;
            const divLoading = document.querySelector('#loadingNotification');
            divLoading.style.display = 'block';

            if (password === rePassword) {
                models.user.register(username, password)
                    .then((response) => {
                        divLoading.style.display = 'none';
                        notification('#successNotification', "You register successfully!", context, '#/user/login');
                    })
                    .catch((e) => {
                        divLoading.style.display = 'none';
                        console.error(e);
                        notification('#errorNotification', "Incorrect email or password!", context);
                    })
            } else{
                divLoading.style.display = 'none';
                notification('#errorNotification', "Both passwords must be the same!", context);
            }
        }
    }
};