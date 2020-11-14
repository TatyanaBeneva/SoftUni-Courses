import { applyCommon } from './common.js';
import {requester} from '../services/app-service.js'
export async function profileHandler() {

    let treks = await requester.treks.getAll();
    this.treks = Object.entries(treks).filter(([trekId, trek]) => trek.createdByName === sessionStorage.getItem('email'));
    this.treks = this.treks.map(([trekId, trek]) => ({...trek, trekId}));
    this.username = sessionStorage.getItem('email');
    this.numberOfTreks = this.treks.length;
    this.isHaveTrek = this.numberOfTreks > 0;
    
    await applyCommon.call(this);
    this.partial('./templates/profile/profile.hbs');
}