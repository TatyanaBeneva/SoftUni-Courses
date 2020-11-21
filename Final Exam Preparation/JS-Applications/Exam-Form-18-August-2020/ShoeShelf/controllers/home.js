import extend from '../utils/helper.js';
import models from '../models/index.js';
import docModifyer from '../utils/docModifyer.js';

export default {
    get: {
        home(context){
            models.shoes.getAll().then((response) => {
                const shoes = response.docs.map(docModifyer);
                shoes.sort((a,b) => a.buyers.length - b.buyers.length);
                context.shoes = shoes;
                extend(context).then(function (){
                    this.partial('../Views/Home/home.hbs');
                })
            })
        }
    }
}