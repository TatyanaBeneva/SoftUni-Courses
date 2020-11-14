import controllers from '../controllers/index.js';

const app = Sammy('#root', function(){
    this.use('Handlebars', 'hbs');

    // Home
    this.get('#/home', controllers.home.get.home);

    // User
    this.get('#/user/login', controllers.user.get.login);
    this.get('#/user/logout', controllers.user.get.logout);
    this.get('#/user/register', controllers.user.get.register);

    this.post('#/user/login', controllers.user.post.login);
    this.post('#/user/register', controllers.user.post.register);

    // Couses
    this.get('#/couse/dashboard', controllers.couses.get.dashboard);
    this.get('#/couse/create', controllers.couses.get.create);
    this.get('#/couse/details/:couseId', controllers.couses.get.details);
    this.get('#/couse/close/:couseId', controllers.couses.del.close);
    this.post('#/couse/donate/:couseId', controllers.couses.put.donate);
    this.post('#/couse/create', controllers.couses.post.create);

});

app.run('#/home');