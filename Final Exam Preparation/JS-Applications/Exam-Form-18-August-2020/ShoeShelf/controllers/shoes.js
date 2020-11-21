import extend from '../utils/helper.js';
import models from '../models/index.js';
import docModifyer from '../utils/docModifyer.js';

export default {
    get: {
        create(context) {
            extend(context).then(function () {
                this.partial('../Views/Shoes/createShoe.hbs');
            })
        },
        details(context) {
            const { shoeId } = context.params;
            models.shoes.get(shoeId).then((response) => {
                const shoe = docModifyer(response);
                Object.keys(shoe).forEach(key => {
                    context[key] = shoe[key];
                });
                context.isCreator = context.creator === localStorage.getItem('email');
                context.isBuyAlready = context.buyers.includes(localStorage.getItem('email'));
                extend(context).then(function () {
                    this.partial('../Views/Shoes/details.hbs');
                })
            });
        },
        edit(context){

            const {shoeId} = context.params;
            models.shoes.get(shoeId).then((response) => {
                const shoe = docModifyer(response);
                Object.keys(shoe).forEach(key => {
                    context[key] = shoe[key];
                });
                extend(context).then(function () {
                    this.partial('../Views/Shoes/editShoe.hbs');
                })
            });
            
        }
    },

    post: {
        create(context) {

            const data = {
                ...context.params,
                uid: localStorage.getItem('userId'),
                buyers: [],
                creator: localStorage.getItem('email')
            };

            models.shoes.create(data).then((response) => {
                context.redirect('#/home');
            }).catch((e) => {
                console.error(e);
            });
        }
    },

    del: {
        delete(context) {
            const { shoeId } = context.params;

            models.shoes.delete(shoeId).then((response) => {
                context.redirect('#/home');
            }).catch(e => {
                console.error(e);
            });
        }
    },

    put: {
        buy(context){
            const { shoeId } = context.params;
            models.shoes.get(shoeId)
                .then((response) => {
                    const shoe = docModifyer(response);
                    shoe.buyers.push(localStorage.getItem('email'));
                    return models.shoes.edit(shoeId, shoe);
                })
                .then((response) => {
                    context.redirect(`#/details/${shoeId}`);
                }).catch(e => {
                    console.error(e);
                });
        },

        edit(context){
            const {shoeId} = context.params;
            const data = {...context.params};
            
            models.shoes.edit(shoeId, data).then((response) => {
                context.redirect(`#/details/${shoeId}`);
            }).catch(e => {
                console.error(e);
            })
        }
    }
}
