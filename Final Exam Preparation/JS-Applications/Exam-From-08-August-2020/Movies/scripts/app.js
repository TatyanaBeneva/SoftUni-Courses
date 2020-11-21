import controllers from '../controllers/index.js';

const app = Sammy('#container', function(){
    this.use('Handlebars', 'hbs');

    // Home
    this.get('#/home', controllers.home.get.home);

    // // User
    this.get('#/user/login', controllers.user.get.login);
    this.get('#/user/logout', controllers.user.get.logout);
    this.get('#/user/register', controllers.user.get.register);

    this.post('#/user/login', controllers.user.post.login);
    this.post('#/user/register', controllers.user.post.register);

    // Movies
    this.get('#/create', controllers.movies.get.create);
    this.get('#/details/:movieId', controllers.movies.get.details);
    this.get('#/like/:movieId', controllers.movies.put.likes);
    this.get('#/delete/:movieId', controllers.movies.del.delete);
    this.get('#/edit/:movieId', controllers.movies.get.edit);
    this.post('#/edit/:movieId', controllers.movies.put.edit);
    this.post('#/create', controllers.movies.post.create);

});

app.run('#/home');