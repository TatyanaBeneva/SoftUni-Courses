const { cookie } = require('../config');

module.exports = (req, res, next) => {
    const token = req.cookies[cookie];

    if(token){
        return res.redirect('/');   
    }

    next();
}