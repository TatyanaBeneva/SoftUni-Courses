import { applyCommon } from './common.js';
import { requester } from '../services/app-service.js';

export async function detailsHandler() {
    /**
     * Gets one team from the db and map it to the expected by the template value + add it to the template context
     * 
     * -- this.params comes from the navigation url!!
     */
    this.trekId = this.params.id;
    let {createdById, createdByName, dateTime, description, imageURL, likes, location} = await requester.treks.getById(this.params.id);
    this.createdById = createdById;
    this.createdByName = createdByName;
    this.dateTime = dateTime;
    this.description = description;
    this.imageURL = imageURL;
    this.likes = likes;
    this.location = location;
    this.userIsCreator = sessionStorage.getItem('userId') === this.createdById;

    /**
     * Load hbs templates
     */
    await applyCommon.call(this);
    this.partial('./templates/details/details.hbs');
}