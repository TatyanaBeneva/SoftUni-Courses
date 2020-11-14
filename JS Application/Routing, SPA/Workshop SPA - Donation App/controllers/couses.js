import extend from '../utils/helper.js';
import models from '../models/index.js';
import docModifyer from '../utils/docModifyer.js';
import notification from '../utils/callNotifications.js';

export default {
    get: {
        dashboard(context) {
            models.couses.getAll().then((response) => {
                const couses = response.docs.map(docModifyer);
                context.couses = couses;
                console.log(couses)
                extend(context).then(function () {
                    this.partial('../views/couse/dashboard.hbs');
                })
            })
        },
        create(context) {
            extend(context).then(function () {
                this.partial('../views/couse/create.hbs');
            })
        },
        details(context) {
            const { couseId } = context.params;
            models.couses.get(couseId).then((response) => {
                const couse = docModifyer(response);
                Object.keys(couse).forEach(key => {
                    context[key] = couse[key];
                });
                context.canDonate = couse.uid !== localStorage.getItem('userId');
                extend(context).then(function () {
                    this.partial('../views/couse/details.hbs');
                })
            });
        }
    },
    post: {
        create(context) {
            const divLoading = document.querySelector('#loadingNotification');
            divLoading.style.display = 'block';

            const data = {
                ...context.params,
                uid: localStorage.getItem('userId'),
                collectedFunds: 0,
                donors: []
            };

            models.couses.create(data).then((response) => {
                divLoading.style.display = 'none';
                notification('#successNotification', "Your cause was created successfully!", context, '#/couse/dashboard');
            }).catch((e) => {
                divLoading.style.display = 'none';
                console.error(e);
                notification('#errorNotification', "Your data is incorrect!", context);
            });
        }
    },
    del: {
        close(context) {
            const divLoading = document.querySelector('#loadingNotification');
            divLoading.style.display = 'block';
            const { couseId } = context.params;

            models.couses.close(couseId).then((response) => {
                divLoading.style.display = 'none';
                    notification('#successNotification', "You closed cause successfully!", context, '#/couse/dashboard');
            }).catch(e => {
                divLoading.style.display = 'none';
                console.error(e);
            });
        }
    },
    put: {
        donate(context) {
            const divLoading = document.querySelector('#loadingNotification');
            divLoading.style.display = 'block';
            const { couseId, currentDonation } = context.params;
            models.couses.get(couseId)
                .then((response) => {
                    const couse = docModifyer(response);
                    couse.collectedFunds += Number(currentDonation);
                    couse.donors.push(localStorage.getItem('email'));
                    return models.couses.donate(couseId, couse);
                })
                .then((response) => {
                    divLoading.style.display = 'none';
                    notification('#successNotification', "Thank you for your donation!", context, '#/couse/dashboard');
                }).catch(e => {
                    divLoading.style.display = 'none';
                    console.error(e);
                    notification('#errorNotification', "Something ment wrong!", context);
                });
        }
    }
};