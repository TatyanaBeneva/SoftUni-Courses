import { applyCommon } from './common.js';
import { requester } from '../services/app-service.js';

export async function homeViewHandler() {
    /**
     * Load hbs templates
     */
    await applyCommon.call(this);
    
    
    let treks = await requester.treks.getAll();
    this.trekId = this.params.id;

    this.treks = Object.entries(treks).map(([trekId, trek]) => ({...trek, trekId}));

    // If we want to visualise only treks, created by the logged user

    // this.treks = [];
    // let mail = sessionStorage.getItem('email');
    // Object.entries(treks).map(([trekId, trek]) => {
    //     let trekMail = trek.createdByName;
    //     if(trekMail === mail){
    //         this.treks.push({...trek, trekId});
    //     }
    // });
    this.partial('./templates/home/home.hbs');
    // successNotification('Please work');
}