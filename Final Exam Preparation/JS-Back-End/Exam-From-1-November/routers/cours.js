const { coursConstroller } = require('../controllers');
const{checkGuestAccess} = require('../utils');
const createCoursValidations = require('../validations/create-cours');

module.exports = (router) => {
    router.get('/create', checkGuestAccess, coursConstroller.get.create);
    router.post('/create', createCoursValidations, coursConstroller.post.create);

    router.get('/details/:id',checkGuestAccess,coursConstroller.get.details);

    router.get('/edit/:id', checkGuestAccess,coursConstroller.get.edit);
    router.post('/edit/:id', coursConstroller.post.edit);

    router.get('/enroll/:id', checkGuestAccess,coursConstroller.get.enroll);

    router.get('/delete/:id', checkGuestAccess,coursConstroller.get.delete);

    return router;
};