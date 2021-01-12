const { userController } = require('../controllers');
const {checkUserAccess, checkGuestAccess} = require('../utils');
const registerValidations = require('../validations/register');
const loginValidations = require('../validations/login');
const login = require('../validations/login');

module.exports = (router) => {
    router.get('/register', checkUserAccess, userController.get.register);
    router.post('/register', registerValidations, userController.post.register);

    router.get('/login', checkUserAccess, userController.get.login);
    router.post('/login', loginValidations, userController.post.login);

    router.get('/logout', checkGuestAccess ,userController.get.logout);

    return router;
};