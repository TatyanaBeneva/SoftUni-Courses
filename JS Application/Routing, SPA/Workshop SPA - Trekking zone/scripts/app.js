import { requester } from './services/app-service.js';
import {
    homeViewHandler,
    loginHandler,
    registerViewHandler,
    logoutHandler,
    detailsHandler,
    editHandler,
    createTrekHandler,
    likesHandler,
    deleteHandler,
    profileHandler
} from './handlers/index.js';

const apiKey = '';
requester.init(apiKey, sessionStorage.getItem('token'));


/**
 * Configure the application with all it's routes and the template engine that it uses 
 */
const app = Sammy('#main', function () {
    /**
     * Setting handlebars as template engine
     */
    this.use('Handlebars', 'hbs');

    /**
     * Define routes to be used by the application
     */
    this.get('#/', homeViewHandler);
    this.get('#/home', homeViewHandler);
    this.get('#/login', loginHandler);
    this.post('#/login', () => false);
    this.get('#/register', registerViewHandler);
    this.post('#/register', () => false);
    this.get('#/logout', logoutHandler);
    this.get('#/details/:id', detailsHandler);
    this.get('#/edit/:id', editHandler);
    this.post('#/edit/:id', () => false);
    this.get('#/create', createTrekHandler);
    this.post('#/create', () => false);
    this.get('#/likes/:currentLikes/:id', likesHandler);
    this.get('#/delete/:id', deleteHandler);
    this.get('#/profile', profileHandler);
});
/**
 * Start the application
 */
app.run('#/');