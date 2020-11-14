import extend from '../utils/helper.js';

export default {
    get: {
        home(context){
            extend(context).then(function (){
                this.partial('../views/home/home.hbs');
            })
        }
    }
}