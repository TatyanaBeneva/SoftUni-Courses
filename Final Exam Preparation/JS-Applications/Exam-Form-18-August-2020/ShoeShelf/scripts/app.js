import controllers from '../controllers/index.js';

const app = Sammy('main', function(){
    this.use('Handlebars', 'hbs');

    // Home
    this.get('#/home', controllers.home.get.home);

    // User
    this.get('#/login', controllers.user.get.login);
    this.get('#/logout', controllers.user.get.logout);
    this.get('#/register', controllers.user.get.register);

    this.post('#/login', controllers.user.post.login);
    this.post('#/register', controllers.user.post.register);

    // Shoes
    this.get('#/create', controllers.shoes.get.create);
    this.get('#/details/:shoeId', controllers.shoes.get.details);
    this.get('#/buy/:shoeId', controllers.shoes.put.buy);
    this.get('#/delete/:shoeId', controllers.shoes.del.delete);
    this.get('#/edit/:shoeId', controllers.shoes.get.edit);
    this.post('#/edit/:shoeId', controllers.shoes.put.edit);
    this.post('#/create', controllers.shoes.post.create);

});

app.run('#/home');