
const handlebars = require('express-handlebars');
const cookieParser = require('cookie-parser')
const { auth } = require('../utils');

module.exports = (express, app) => {
    app.use(express.static('static'))
    app.use(express.json());
    app.use(express.urlencoded({ extended: true}));

    app.use(cookieParser());
    app.use(auth);
      
    app.engine('.hbs', handlebars({
        layoutsDir: 'views',
        defaultLayout: 'main.hbs',
        partialsDir: 'views/partials',
        extname: '.hbs'
    }));
    app.set('view engine', '.hbs');   

};