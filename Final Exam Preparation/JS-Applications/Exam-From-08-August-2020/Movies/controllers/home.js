import extend from '../utils/helper.js';
import models from '../models/index.js';
import docModifyer from '../utils/docModifyer.js';

export default {
    get: {
        home(context){
            models.movies.getAll().then((response) => {
                const movies = response.docs.map(docModifyer);
                context.movies = movies;
                extend(context).then(function (){
                    this.partial('../Views/Home/home.hbs');
                })
            })
        }
    }
}